from django.shortcuts import render
from django.http import HttpResponse

from .models import TodoItem


def index(request):

    todo_items = TodoItem.objects.all()
    # print(todo_items)

    # output = '<ul>'
    # # output += ''.join([f'<li>{todo_item.text}</li>' for todo_item in todo_items])
    # for todo_item in todo_items:
    #     output += f'<li>{todo_item.text}</li>'
    # output += '</ul>'

    # return HttpResponse(output)

    context = {'todo_items': todo_items}
    return render(request, 'todoapp/index.html', context)





def about(request):
    return render(request, 'todoapp/about.html')