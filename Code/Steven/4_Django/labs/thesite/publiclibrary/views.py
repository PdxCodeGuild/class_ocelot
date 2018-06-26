from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index(request):

    # Get all the books from the database, ordered by id
    books = Book.objects.all()

    # Put all the books in a dictionary
    context = {'books':books}

    # Note: In template, loop over the elements of the 'books' dict, generate a <tr> for each book

    return render(request, 'publiclibrary/index.html', context)

