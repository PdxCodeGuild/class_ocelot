from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.db.models.functions import Length
from django.urls import reverse
import django.shortcuts
from .models import Author, Book, Checkout

def home(request):
    books = Book.objects.order_by('author__last_name')
    authors = Author.objects.order_by('last_name')
    ctx = {'books': books,
           'authors': authors}
    return render(request, 'library/home.html', ctx)

def filter_title(request):
    search_text = request.GET['search_title']
    if search_text == 'all':
        books = Book.objects.order_by('author__last_name')
    else:
        books = Book.objects.filter(title__icontains=search_text)
    data = {'books': []}
    for book in books:
        data['books'].append(book.toDictionary())
    return JsonResponse(data)

def filter_author(request):
    search_text = request.GET['search_author']
    books = Book.objects.filter(author=search_text)
    data = {'books': []}
    for book in books:
        data['books'].append(book.toDictionary())
    return JsonResponse(data)

def checkout(request):
    return HttpResponse('hi')

    # def book_detail(request, book_id):
    #
    #
    # new_long = request.POST['user_']
    # new_short = shortURL()
    # new_URL = URL(long_url=new_long, short_url=new_short)
    # new_URL.save()
    # urls = URL.objects.order_by(Length('long_url').asc())
    # return render(request, 'shortener/index.html', {'urls': urls})