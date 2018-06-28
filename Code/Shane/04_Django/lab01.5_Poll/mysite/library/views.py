from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Author, Book, Checkout
from django.urls import reverse
from django.utils import timezone


# Create your views here.

def index(request):
    # return HttpResponse("hi there")
    authors = Author.objects.all()
    books = Book.objects.all()
    users = Checkout.objects.all()

    context = {
        'authors_key': authors,
        'books_key': books,
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



def checkout(request):
    #add the name of the person that checked out the book to the model
    checkout_person = request.POST['person']
    book_id = request.POST['book_id']
    checkout = Checkout(user=checkout_person, book_id=book_id)
    checkout.save()


    #need to change the check-out button to check-in
    #Remove the input field and print the name of the person that has the book checked out


    return HttpResponseRedirect(reverse('library:index'))


def checkin(request):
    book_id = request.POST['book_id']
    checkout = Checkout.objects.get(book_id=book_id, checkin__isnull=True)
    checkout.checkin = timezone.now()
    checkout.save()
    return HttpResponseRedirect(reverse('library:index'))



