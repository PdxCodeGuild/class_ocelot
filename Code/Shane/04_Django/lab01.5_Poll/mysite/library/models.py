from django.db import models
from django.utils import timezone


# Create your models here.


    # Many authors can have many books
class Author(models.Model):
    author_name = models.CharField(max_length=50)


    def __str__(self):
        return self.author_name


    # Many books can have many authors otherwords many authors id will be on many books
class Book(models.Model):
    book_title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)

    def checked_out_user(self):
        checkout = self.checkout_set.get(checkin__isnull = True)
        return checkout.user

    def checked_out(self):
        return self.checkout_set.filter(checkin__isnull=True).exists()

    def author_list(self):
        return ', '.join([author.author_name for author in self.authors.all()])

    def __str__(self):
        return self.book_title



class Checkout(models.Model):
    checkout = models.DateTimeField(auto_now_add=True)
    checkin = models.DateTimeField(null=True, blank=True)
    user = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


