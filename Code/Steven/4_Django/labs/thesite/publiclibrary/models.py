from django.db import models
# from django.contrib.auth.models import Author


# One Author can write many Books
class Author(models.Model):
    name = models.CharField( max_length=50)

    def __str__(self):
        return self.name


# One Book can be written by many Authors (ONLY ONE AUTHOR CURRENTLY)
class Book(models.Model):
    title = models.CharField( max_length=50)
    publish_date = models.DateTimeField()
    checkedout_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE)

    def checked_out(self):
        return self.checkedout_date is not None

    def __str__(self):
        return self.title
    #
    # def author(self):
    #     return self.book.author


class User(models.Model):
    name = models.CharField( max_length=50)
    number = models.IntegerField()
    checkedout_items = models.ForeignKey(
        Book, on_delete=models.CASCADE)

