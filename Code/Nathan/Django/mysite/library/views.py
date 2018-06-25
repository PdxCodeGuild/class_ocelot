from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Author, Book
# Create your views here.

def index(request):
    context = {'authors': Author.objects.all()}
    return render(request, 'library/index.html', context)


def author_lookup(request):
    author_search = request.GET['author_search']
    author = Author.objects.get(name=author_search)
    print(author.book_set.all())

    return HttpResponseRedirect(reverse('library:index'))

