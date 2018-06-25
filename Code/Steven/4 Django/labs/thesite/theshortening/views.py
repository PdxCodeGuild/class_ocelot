from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from .models import UrlList
from django.http import HttpResponseRedirect

import string, random


# from .forms import UrlInputForm

# View 1: Render the index page
def index(request):

    # get all the LongUrls from the database

    # long_urls = UrlList.objects.all() # pre-reversal
    long_urls = UrlList.objects.order_by('-id')


    # put that in a dictionary
    context = {'long_urls':long_urls}
    # in your template, loop over the elements, generate a tr for each

    return render(request, 'theshorteningapp/index.html', context)


# View 2: Receive the submission
def save_url(request):
    # print(request.POST)
    url = request.POST['url']
    # generate a random code (password generator lab)

    short_code = ''
    for rnd_char in range(12):
        short_code += random.choice(string.digits + string.ascii_letters + string.digits)

    # create an instance of the model
    long_url = UrlList(url=url, code=short_code)

    # save the instance of the model
    long_url.save()

    # redirect back to the index page
    return HttpResponseRedirect(reverse('theshortening:index'))

# View 3: Return redirect (?)
def redeem_shortcode(request, code):
    table_of_urls = UrlList.objects.get(code=code)
    return redirect(table_of_urls.url)


    # return HttpResponse('the redeem_shortcode')