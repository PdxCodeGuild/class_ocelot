from django.db import models


# Create your models here.


    # Many authors can have many books
class Author(models.Model):
    author_name = models.CharField(max_length=50)



    def __str__(self):
        return self.author_name

    # Many books can have many authors
class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(author_name=author_name)


    def __str__(self):
        return self.title


class Checkout(models.Model):
    checkout_name = models.CharField(max_length=200)

    def __str__(self):
        return self.checkout_name
