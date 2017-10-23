from __future__ import unicode_literals

from django.db import models

import re
emailREGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
# class UserManager(models.Manager):
#     def basic_validator(self, postData):
#         errors = {}
#         if len(postData['inputted_name']) < 5:
#             errors["name"] = "Blog name should be more than 5 characters"
#         if not emailREGEX.match(postData['inputted_email']):
#             errors["email"] = "Email must be in proper format"
#         return errors;
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 1 or len(postData['alias']) < 1 or len(postData['email']) < 1 or len(postData['password']) < 1 or len(postData['confirm_password']) < 1:
            errors["all"] = "All fields must be filled"
            return errors
        if len(postData['name']) < 3:
            errors["name"] = "Name should be more than 2 characters"
        if len(postData['alias']) < 3:
            errors["alias"] = "Alias should be more than 2 characters"
        if not emailREGEX.match(postData['email']):
            errors["email"] = "Email must be in proper format"
        if len(postData['password']) < 8:
            errors["password_length"] = "Password must be at least 8 characters long"
        if postData['password'] != postData['confirm_password']:
            errors["password"] = "Password must match"
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __repr__(self):
        return "<User object: {}>".format(self.name)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    uploaded_user = models.ForeignKey(User, related_name="uploaded_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Book object: {}>".format(self.title)

class Book_Review(models.Model):
    message = models.TextField()
    rating = models.IntegerField()
    belong_to = models.ForeignKey(Book, related_name="book_reviews")
    reviewed_by = models.ForeignKey(User, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Review object: {}>".format(self.message)