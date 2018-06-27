from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
# book = Book.objects.get(pk=1)
# book.author.name
# author.book_set.all() or .order_by()

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateField()
    author = models.ForeignKey(Author, on_delete='CASCADE')

    def __str__(self):
        return self.title

class Checkout(models.Model):
    user = models.TextField()
    book = models.ForeignKey(Book, on_delete='CASCADE')
    checkout_date = models.DateTimeField(auto_now_add=True)
    checkin_date = models.DateTimeField(null=True, blank=True)

    def checkin(self):
        self.checkin_date = timezone.now()



