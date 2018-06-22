import random
import string

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ShortUrl
from django.urls import reverse


# Create your views here.

def index(request):
    # return HttpResponse("hi")

    show_short_codes = ShortUrl.objects.all()

    newthing = ShortUrl.objects.get(short_url='1stShort')

    context = {
        'show_short_codes': show_short_codes,
        'newthing': newthing
    }

    return render(request, 'short_url/index.html', context)


def random_code_gen():
    code = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)])
    return code

    # go to the bd and get the display      ... ... ...objects.all()


def add_url(request):
    print(request)
    short_url = random_code_gen()
    long_url = request.POST['long_url_text']
    url_text = ShortUrl(short_url = short_url, long_url = long_url)
    url_text.save()
    # item_on_list = question.choice_set.get(pk=request.POST['choice'])
    # save data from request.POST in database
    # redirect back to the index page (HttpResponseRedirect)

    return HttpResponseRedirect(reverse('short_url:index'))


def short_code(request, url_code):
    short_url = ShortUrl.objects.get(short_url=url_code)
    return redirect(short_url.long_url)


# ######
# def remove_todo(request):
#     todo_text = request.POST['todo_item_id_key_in_template']
#     todo_item = ShortUrl.objects.get(pk = todo_text)
#     todo_item.delete()
#     # item_on_list = question.choice_set.get(pk=request.POST['choice'])
#     # save data from request.POST in database
#     # redirect back to the index page (HttpResponseRedirect)
#
#     return HttpResponseRedirect(reverse('short_url:index'))
