from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Book, Author


def index(request): # the 'default' view
    books = Book.objects.all() # Get all the books from the database, ordered by id
    cat_total = Book.objects.all().count() # Count all books in the database
    cat_in = Book.objects.filter(checkedout_date__isnull=False).count() # Count all books NOT in 'checked out list'
    cat_out = Book.objects.filter(checkedout_date__isnull=True).count() # Count all the books IN 'checked out list'
    author_total = Author.objects.all().count() # Get all the authors in the Author database
    context = {'books': books,
               'cat_total': cat_total,
               'cat_in': cat_in,
               'cat_out': cat_out,
               'author_total': author_total
               }

    # Note: In template, loop over the elements of the 'books' dict, generate a <tr> for each book
    return render(request, 'publiclibrary/index.html', context) # this is the path provided to the browser (via template)

def checkout_book(request):
    # print(request.POST['book_id']) # TESTING
    book_id = request.POST['book_id'] # Receive book id from 'dictionary-like object' returned from form
    checked_out_book = Book.objects.get(pk=book_id) # Use book id to get book from database (via model)
    checked_out_book.checkedout_date = timezone.now()  # set the checkout date on the book timezone.now
    checked_out_book.save()  # save the book, with new 'checked out date', to database (via model)
    return HttpResponseRedirect(reverse('publiclibrary:index')) # redirect back to the index page


def checkin_book(request):
    book_id = request.POST['book_id']
    checked_in_book = Book.objects.get(pk=book_id)
    checked_in_book.checkedout_date = None
    checked_in_book.save()
    return HttpResponseRedirect(reverse('publiclibrary:index'))
