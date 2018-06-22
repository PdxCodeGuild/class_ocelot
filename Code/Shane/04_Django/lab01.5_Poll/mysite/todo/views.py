from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
from django.urls import reverse

# Create your views here.

def index(request):
    somevar = TodoItem.objects.all()

    context = {
        'todo_items123': somevar
            # somevar[0].todo_text #<-- This is from models column 1 named todo_text
    }

    return render(request, 'todo/index.html', context)
    # go to the bd and get the display      ... ... ...objects.all()

def add_todo(request):
    todo_text = request.POST['todo_item']
    todo_item = TodoItem(todo_text=todo_text, completed=False)
    todo_item.save()
    # item_on_list = question.choice_set.get(pk=request.POST['choice'])
    # save data from request.POST in database
    # redirect back to the index page (HttpResponseRedirect)

    return HttpResponseRedirect(reverse('todo:index'))

def remove_todo(request):
    todo_text = request.POST['todo_item_id_key_in_template']
    todo_item = TodoItem.objects.get(pk = todo_text)
    todo_item.delete()
    # item_on_list = question.choice_set.get(pk=request.POST['choice'])
    # save data from request.POST in database
    # redirect back to the index page (HttpResponseRedirect)

    return HttpResponseRedirect(reverse('todo:index'))
