from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader

# Create your views here.

def index(request):
        #if request == POST:

    # get all the todo items out of the database
    # pass those as part of the context to render the template
    return render(request, 'todo/index.html', {'name':'joanne'})
    # go to the bd and get the display      ... ... ...objects.all()

def add_todo(request):
    # save data from request.POST in database
    # redirect back to the index page (HttpResponseRedirect)
    return HttpResponse('add todo!!!')