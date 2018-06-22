from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import json
from .models import TodoAjaxItem

def index(request):
    return render(request, 'todoajax/index.html', {})


def add_todo(request):
    data = json.loads(request.body)
    todo_item = TodoAjaxItem(text=data['todo_text'])
    todo_item.save()

    return get_todos(request)


def get_todos(request):

    todo_items = TodoAjaxItem.objects.all()
    data = {'todo_items': []}
    for todo_item in todo_items:
        data['todo_items'].append(todo_item.toDictionary())

    return JsonResponse(data)