from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader

# Create your views here.

def index(request):
    context = {
        'HI THERE'
    }
    return HttpResponse(context)

