from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from .models import Todo

def index(request):
    latest_todo_list = Todo.objects.order_by('-pub_date')
    context = {
        'todo_list': latest_todo_list,
    }
    return render(request, 'todo/index.html', context)

def add_todo(request):
    todo_text = request.POST['todo']
    # create a to do item
    todo_item = Todo(todo_text=todo_text, pub_date=timezone.now())
    # save it
    todo_item.save()
    # redirect back to the index page
    return HttpResponseRedirect(reverse('todo:index'))