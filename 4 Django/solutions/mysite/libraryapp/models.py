from django.db import models


class AuthorMTO(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        # author_id = self.id
        # books = BookMTO.objects.filter(author_id=author_id)

        books = [book.name for book in self.books.all()]
        return self.name + '- ' + ', '.join(books)


class BookMTO(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(AuthorMTO, on_delete=models.SET_NULL, related_name='books', null=True, blank=True)

    def __str__(self):
        return f'{self.author_id} {self.author.name} - {self.name}'



# authors1 = AuthorMTO.objects.all()
# for author1 in authors1:
#     author2 = AuthorMTM(name=author1.name)
#     author2.save()
#


class AuthorMTM(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class BookMTM(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(AuthorMTM, related_name='books')

    def __str__(self):
        return self.title





