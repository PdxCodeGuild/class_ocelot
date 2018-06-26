from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Author, Book


# Create your views here.

def index(request):
    # return HttpResponse("hi there")
    author = Author.objects.all()
    book = Book.objects.all()

    context = {
        'author': author,
        'book': book
    }

    return render(request, 'library/index.html', context)

