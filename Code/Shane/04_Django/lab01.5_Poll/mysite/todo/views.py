from .models import TodoItem
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .decorators import check_recaptcha
import requests
from django.conf import settings
from django.contrib import messages
import json
import urllib


# Create your views here.


@login_required
def index(request):
    somevar = request.user.todoitem_set.all()

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
    todo_item = TodoItem.objects.get(pk=todo_text)
    todo_item.delete()
    # item_on_list = question.choice_set.get(pk=request.POST['choice'])
    # save data from request.POST in database
    # redirect back to the index page (HttpResponseRedirect)

    return HttpResponseRedirect(reverse('todo:index'))

@check_recaptcha
def register(request):
    if not request.recaptcha_is_valid:
        return HttpResponseRedirect(reverse('todo:login_register')+'?message=bad_recaptcha')
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    login(request, user)
    return HttpResponseRedirect(reverse('todo:index'))


@check_recaptcha
def mylogin(request):
    if not request.recaptcha_is_valid:
        return HttpResponseRedirect(reverse('todo:login_register')+'?message=bad_recaptcha')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)


    if user is not None:
        login(request, user)
        if 'next' in request.POST and request.POST['next'] != '':
            return HttpResponseRedirect(request.POST['next'])
        return HttpResponseRedirect(reverse('todo:index'))
    return HttpResponseRedirect(reverse('todo:login_register'))


def mylogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('todo:login_register'))



def login_register(request):
    message = request.GET.get('message', '')
    next = request.GET.get('next', '')
    return render(request, 'todo/login_register.html', {'next': next, 'message': message})
