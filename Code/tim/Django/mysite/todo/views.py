
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import random
from .models import TodoItem, TotoItem, TodoList

def home(request):
    lists = TodoList.objects.order_by('-created')
    return render(request, 'todo/home.html', {'lists': lists})

def list(request, list_id):
    list = get_object_or_404(TodoList, pk=list_id)
    ordered_list = list.todoitem_set.order_by('-due_date')
    print(list)
    print(ordered_list)
    return render(request, 'todo/list.html', {'list': list, 'items': ordered_list})

def add(request, list_id):
    toto = random.choice(TotoItem.objects.all())
    # got_list = TodoList.objects.get(pk=list_id)
    new_todo = TodoItem(
        list_id = list_id,
        item_text = request.POST['item_text'],
        due_date = request.POST['due_date'],
        urgency = request.POST['urgency'],
        toto_item = toto)
    new_todo.save()
    return HttpResponseRedirect(reverse('todo:list', args=(list_id,)))
