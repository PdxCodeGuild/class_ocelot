from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
import random
import string

from .models import Shortener

def index(request):

    return render(request, 'urlredirect/index.html')


def get_random_code():
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(6)])


# def get_random_unique_code():
#     code = get_random_code()
#     while Shortener.objects.get(code=code) is not None:
#         code = get_random_code()
#     return code


def save_shortener(request):
    full_url = request.POST['furl']
    code = get_random_code()
    shortener = Shortener(code=code, urls=full_url)
    shortener.save()

    return HttpResponseRedirect(reverse('urlredirect:index'))


def random_code(request):

    return redirect(object)