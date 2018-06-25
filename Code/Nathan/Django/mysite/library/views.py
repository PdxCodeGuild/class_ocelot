from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Author, Book
# Create your views here.

def index(request):

    print(request.GET)

    if 'author_id' in request.GET:
        author_id = request.GET['author_id']
        author = Author.objects.get(pk=author_id)
        books = author.book_set.all()
    else:
        books = Book.objects.all()
    authors = Author.objects.all()

    context = {'authors': authors, 'books': books}
    return render(request, 'library/index.html', context)

# def author_lookup(request):
#
#     # author_search = request.GET['author_search']
#     # author = Author.objects.get(name=author_search)
#     # print(author.book_set.all())
#     # output = Book.objects.filter(title=author.id) \
#     #          | Book.objects.filter(publish_date=author.id)
#
#
#
#     return HttpResponseRedirect(reverse('library:index'))
#
