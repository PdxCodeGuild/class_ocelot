from django.shortcuts import render
from django.http import HttpResponse
from .models import LongUrl
from django.http import HttpResponseRedirect


# from .forms import UrlInputForm

# View 1: Render the index page
def index(request):
    return render(request, 'theshorteningapp/index.html')


# View 2: Receive the submission
def save_url(request):
    # print(request.POST)
    url = request.POST['url']
    # generate a random code (password generator lab)
    # create an instance of the model
    # save it
    # redirect back to the index page
    return HttpResponse('this is get_long_url')

# View 3: Return redirect (?)
def repointer(request):
    # from django.urls import reverse
    # def add ( request ):
    #     return HttpResponseRedirect ( reverse ( 'theshortening:repointer' ) )
    #

    return HttpResponse('the repointer')