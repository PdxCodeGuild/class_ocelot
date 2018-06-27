from django.db import models
from django.utils import timezone


# Create your models here.


    # Many authors can have many books
class Author(models.Model):
    author_name = models.CharField(max_length=50)

    def __str__(self):
        return "Author: " + self.author_name


    # Many books can have many authors otherwords many authors id will be on many books
class Book(models.Model):
    book_title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return "Title: " + self.book_title



class Checkout_in(models.Model):
    checkedout = models.BooleanField(default=False)
    checkout_in = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    checkout_out = models.DateTimeField(auto_now_add = True, null=True, blank=True)

    def __str__(self):
        return "Checkedout " + self.checkedout


