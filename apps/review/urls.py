from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_user$', views.add_user),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^books$', views.books_home),
    url(r'^add$', views.add),
    url(r'^add_book$', views.add_book),
    url(r'^add_review$', views.add_review),
    url(r'^book/(?P<book_id>\d+)$', views.book_detail),
]