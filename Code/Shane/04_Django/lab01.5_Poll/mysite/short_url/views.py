from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ShortUrl
from django.urls import reverse

# Create your views here.

def index(request):

    return HttpResponse("It's alive")
    # show_short_codes = ShortUrl.objects.short_url()

    # context = {
    #     'todo_items123': show_short_codes
    # }

    # return render(request, 'short_url/index.html', context)
    # go to the bd and get the display      ... ... ...objects.all()
#
# def add_todo(request):
#     todo_text = request.POST['todo_item']
#     todo_item = ShortUrl(todo_text=todo_text, completed=False)
#     todo_item.save()
#     # item_on_list = question.choice_set.get(pk=request.POST['choice'])
#     # save data from request.POST in database
#     # redirect back to the index page (HttpResponseRedirect)
#
#     return HttpResponseRedirect(reverse('short_url:index'))
#
# def remove_todo(request):
#     todo_text = request.POST['todo_item_id_key_in_template']
#     todo_item = ShortUrl.objects.get(pk = todo_text)
#     todo_item.delete()
#     # item_on_list = question.choice_set.get(pk=request.POST['choice'])
#     # save data from request.POST in database
#     # redirect back to the index page (HttpResponseRedirect)
#
#     return HttpResponseRedirect(reverse('short_url:index'))
