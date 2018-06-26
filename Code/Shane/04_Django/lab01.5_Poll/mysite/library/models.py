from django.db import models


# Create your models here.

class Author(models.Model):
    author_name = models.CharField(max_length=50)

    def __str__(self):
        return self.library


class Book(models.Model):
    book_name = models.CharField(max_length=200)

    def __str__(self):
        return self.library
