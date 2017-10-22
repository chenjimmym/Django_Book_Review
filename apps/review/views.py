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
            print "REGISTERED@@@@@@"
            return redirect('/')