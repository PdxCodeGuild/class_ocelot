from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models.functions import Length
from django.urls import reverse
import django.shortcuts  # me! me! I have redirect!
import string, random
from .models import URL

def shortURL():
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(6))

def index(request):
    urls = URL.objects.order_by(Length('long_url').asc())
    return render(request, 'shortener/index.html', {'urls': urls})

def saveurl(request):
    print(request)
    new_long = request.POST['long_url']
    new_short = shortURL()
    new_URL = URL(long_url=new_long, short_url=new_short)
    new_URL.save()
    urls = URL.objects.order_by(Length('long_url').asc())
    return render(request, 'shortener/index.html', {'urls': urls})

def redirect(request, short_url):
    long_url_obj = URL.objects.get(short_url=short_url)
    return django.shortcuts.redirect(long_url_obj.long_url)
