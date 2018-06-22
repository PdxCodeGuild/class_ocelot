from django.shortcuts import render, reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from .models import TodoItem


def index(request):

    todo_items = TodoItem.objects.order_by('date_completed', '-date_created')
    # for todo_item in todo_items:
    #     print(todo_item)
    context = {'todo_items': todo_items}
    return render(request, 'todoapp/index.html', context)


def add_todo(request):
    # get the todo_text from the submitted for data
    todo_text = request.POST['todo_text']
    todo_item = TodoItem(text=todo_text)
    todo_item.save()

    return HttpResponseRedirect(reverse('todoapp:index'))

def complete_todo(request):
    todo_item_id = request.POST['todo_item_id']
    todo_item = TodoItem.objects.get(pk=todo_item_id)
    todo_item.date_completed = timezone.now()
    todo_item.save()
    return HttpResponseRedirect(reverse('todoapp:index'))


