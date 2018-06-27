from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Author, Book
from django.urls import reverse


# Create your views here.

def index(request):
    # return HttpResponse("hi there")
    authors = Author.objects.all()
    books = Book.objects.all()

    context = {
        'authors_key': authors,
        'books_key': books
    }

    return render(request, 'library/index.html', context)



def add_book_and_author(request):
    print(request)
    author_text = request.POST['author_input']
    book_text = request.POST['book_input']

    # check if exists, if not, create
    # for book and author

    try:
        author = Author.objects.get(author_name=author_text)
    except Author.DoesNotExist:
        author = Author(author_name=author_text)
        author.save()

    try:
        book = Book.objects.get(book_title=book_text)
    except Book.DoesNotExist:
        book = Book(book_title=book_text)
        book.save()

    book.authors.add(author)
    book.save()

    return HttpResponseRedirect(reverse('library:index'))






