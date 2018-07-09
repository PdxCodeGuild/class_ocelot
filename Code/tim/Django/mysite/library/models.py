import datetime
from django.db import models
from django.utils import timezone

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    fav_color = models.CharField(max_length=100)

    def __str__(self):
        return self.last_name + ', ' + self.first_name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    pub_date = models.DateField()

    def __str__(self):
        return self.title + ' (' + self.author.last_name + ')'

    def yearPublished(self):
        return self.pub_date.year

    def toDictionary(self):
        return {'author': str(self.author),
                'title': self.title,
                'year': self.yearPublished()}

class Checkout(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_out = models.DateField()
    date_in = models.DateField(null=True, blank=True)


