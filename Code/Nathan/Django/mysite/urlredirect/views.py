from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
import random
import string

from .models import Shortener

def index(request):
    context = {'shorteners': Shortener.objects.all()}
    return render(request, 'urlredirect/index.html', context)

def get_random_code():

    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(6)])

def save_shortener(request):

    full_url = request.POST['furl']
    code = get_random_code()
    shortener = Shortener(code=code, urls=full_url)
    shortener.save()

    return HttpResponseRedirect(reverse('urlredirect:index'))
    # return HttpResponseRedirect('urlredirect:index')


def short_url_redirect(request, code):
    # find the Shortener with this code
    shortener = Shortener.objects.get(code=code)

    return redirect(shortener.urls)

def redirect_form(request):
    code = request.POST['code']
    shortener = Shortener.objects.get(code=code)

    return redirect(shortener.urls)

