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
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def checked_out(self):
        return self.checkout_set.filter(checkin_date__isnull=True).exists()


    def __str__(self):
        return self.title

class Checkout(models.Model):
    user = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True)
    checkin_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user + ' ' + self.book.title

    def checkin(self):
        self.checkin_date = timezone.now()



