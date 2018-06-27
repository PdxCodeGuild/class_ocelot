from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Book


def index(request):

    # Get all the books from the database, ordered by id
    books = Book.objects.all()

    # Put all the books in a dictionary
    context = {'books':books}

    # Note: In template, loop over the elements of the 'books' dict, generate a <tr> for each book

    return render(request, 'publiclibrary/index.html', context)

def checkout_book(request):
    # print(request.POST['book_id'])

    # get the book with the given book id
    book_id = request.POST['book_id']
    checked_out_book = Book.objects.get(pk=book_id)
    print(checked_out_book)

    # set the checkout date on the book timezone.now
    checked_out_book.checkedout_date = timezone.now()

    checked_out_book.save()

    # save the book


    # redirect back to the index page

    return HttpResponseRedirect(reverse('publiclibrary:index'))

