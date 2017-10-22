from django.shortcuts import render, redirect, HttpResponse
from models import *
from django.contrib import messages
# Create your views here.
def index(request):
    response = 'it is connected'
    return render(request, 'review/index.html')

def add_user(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for error in errors.itervalues():
                messages.error(request, error)
            return redirect('/')
        else:
            # name = request.POST['name']
            User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=request.POST['password'])
            return redirect('/')

def login(request):
    if request.method == 'POST':
        if not 'login_status' in request.session:
            request.session['login_status'] = False
        login_data = User.objects.filter(email=request.POST['email'])
        request.session['login_status'] = {'name':login_data.first().name, 'alias':login_data.first().alias, 'email':login_data.first().email}
        print request.session['login_status']
        return redirect('/')