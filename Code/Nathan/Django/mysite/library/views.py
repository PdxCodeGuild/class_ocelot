from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Author, Book , Checkout
from django.utils import timezone
# Create your views here.

def index(request):

    print(request.GET)

    if 'author_id' in request.GET:
        author_id = request.GET['author_id']

        if author_id == 'show_all':
            books = Book.objects.all()
        else:
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

def checkout(request, book_id):
    print(request.POST)

    user = request.POST['user_name']

    book = Book.objects.get(pk=book_id)
    # create a checkout object
    time_out = timezone.now()
    checkout = Checkout(user=user, book=book, checkout_date=time_out)
    checkout.save()
    print(checkout.book)


    return HttpResponseRedirect(reverse('library:index'))
    # HttpResponse('ok')

def checkin(request, book_id):
    print(request.POST)

    user = request.POST['user_name']

    # find the Checkout for this book whose check in date is none\
    # book = Book.objects.get(pk=book_id)
    # checkout = book.checkout_set.get(checkin_date__isnull=True)

    checkout = Checkout.objects.get(book_id=book_id, checkin_date__isnull=True)


    checkout.checkin_date = timezone.now()
    checkout.save()


    return HttpResponseRedirect(reverse('library:index'))