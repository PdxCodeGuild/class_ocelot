
from .models import TodoItem
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
    somevar = TodoItem.objects.all()

    context = {
        'todo_items123': somevar
            # somevar[0].todo_text #<-- This is from models column 1 named todo_text
    }

    return render(request, 'todo/index.html', context)
    # go to the bd and get the display      ... ... ...objects.all()

@login_required
def add_todo(request):
    todo_text = request.POST['todo_item']
    todo_item = TodoItem(todo_text=todo_text, user=request.user, completed=False)
    todo_item.save()
    # item_on_list = question.choice_set.get(pk=request.POST['choice'])
    # save data from request.POST in database
    # redirect back to the index page (HttpResponseRedirect)

    return HttpResponseRedirect(reverse('todo:index'))

@login_required
def remove_todo(request):
    todo_text = request.POST['todo_item_id_key_in_template']
    todo_item = TodoItem.objects.get(pk = todo_text)
    todo_item.delete()
    # item_on_list = question.choice_set.get(pk=request.POST['choice'])
    # save data from request.POST in database
    # redirect back to the index page (HttpResponseRedirect)

    return HttpResponseRedirect(reverse('todo:index'))


def register(request):
    return HttpResponse('register here')


def mylogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('todo:index'))


def mylogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('todo:index'))
    else:
        return HttpResponseRedirect(reverse('todo:index'))


def login_register(request):
    next = request.GET.get('next', '')
    return render(request, 'userapp/login_register.html', {'next': next})
