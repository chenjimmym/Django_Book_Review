from django.shortcuts import render, redirect, HttpResponse
from models import *
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):
    # Book.objects.all().delete
    return render(request, 'review/index.html')

def add_user(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for error in errors.itervalues():
                messages.error(request, error)
            return redirect('/')
        else:
            password = request.POST['password']
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'], password=hashed_password)
            messages.error(request, "Successfully Registered")
            return redirect('/')

def login(request):
    if request.method == 'POST':
        if not 'login_status' in request.session:
            request.session['login_status'] = False
        login_data = User.objects.filter(email=request.POST['email'])
        inputted_password = request.POST['password']
        stored_password = User.objects.filter(email=request.POST['email']).first().password
        if login_data and bcrypt.checkpw(inputted_password.encode(), stored_password.encode()):
            request.session['login_status'] = {'id':login_data.first().id, 'name':login_data.first().name, 'alias':login_data.first().alias, 'email':login_data.first().email}
            return redirect('/books')
        else:
            messages.error(request, "Email and password does not match")
            return redirect('/')

def logout(request):
    request.session['login_status'] = False
    return redirect('/')

def books_home(request):
    recent_reviews = Book_Review.objects.order_by("-updated_at")[:3]
    all_books = Book.objects.all()
    context = {
        'recent_reviews': recent_reviews,
        'all_books': all_books
    }
    return render(request, 'review/books.html', context)

def add(request):
    return render(request, 'review/add_book.html')

def add_book(request):
    if request.method == 'POST':
        temp = Book.objects.create(title=request.POST['book_title'], author=request.POST['author'], uploaded_user_id=request.session['login_status']['id'])
        Book_Review.objects.create(message=request.POST['review'], rating=request.POST['rating'], belong_to_id=temp.id, reviewed_by_id=request.session['login_status']['id'])
    url = '/book/' + str(temp.id)
    return redirect(url)

def book_detail(request, book_id):
    title = Book.objects.get(id=book_id).title
    author = Book.objects.get(id=book_id).author
    reviews = Book_Review.objects.filter(belong_to_id=book_id)
    # query = "SELECT * FROM review_user JOIN review_book ON review_user.id = uploaded_user_id JOIN review_book_review ON belong_to_id = review_book.id WHERE belong_to_id =" + book_id
    # reviews = Book.objects.raw(query)
    # print reviews[0].name
    context = {
        'title':title,
        'author':author,
        'reviews':reviews,
        'book_id':book_id
    }
    return render(request, 'review/book_detail.html', context)

def user_detail(request, user_id):
    user_info = User.objects.get(id=user_id)
    user_reviews = User.objects.get(id=user_id).reviews.all()
    review_count = len(user_reviews)
    print user_reviews
    context = {
        'user_info': user_info,
        'user_reviews': user_reviews,
        'review_count': review_count
    }
    return render(request, 'review/user_detail.html', context)

def add_review(request):
    if request.method == 'POST':
        Book_Review.objects.create(message=request.POST['message'], rating=request.POST['rating'], belong_to_id=request.POST['book_id'], reviewed_by_id=request.session['login_status']['id'])
    url = '/book/' + request.POST['book_id']
    return redirect(url)

def delete_review(request):
    print request.POST['book_id']
    print request.POST['review_id']
    Book_Review.objects.get(id=request.POST['review_id']).delete()
    url = '/book/' + request.POST['book_id']
    return redirect(url)