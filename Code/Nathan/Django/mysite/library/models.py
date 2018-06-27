from django.db import models

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
