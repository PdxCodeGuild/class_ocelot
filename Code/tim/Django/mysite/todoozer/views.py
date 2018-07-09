from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
import random
from .models import TodoItem, TotoItem, TodoList
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required


def login_register(request):
    next = request.GET.get('next', '')
    return render(request, 'todoozer/login_register.html', {'next': next})

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if 'next' in request.POST and request.POST['next'] != '':
            return redirect(request.POST['next'])
        return redirect(reverse('todoozer:home'))
    return redirect(reverse('todoozer:login_register'))

def logout_view(request):
    logout(request)
    return redirect(reverse('todoozer:login_register'))

def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    login(request, user)
    return redirect(reverse('todoozer:home'))

@login_required
def home(request):
    selected_list_id = request.GET.get('selected_list_id', '')
    lists = TodoList.objects.filter(user_id=request.user.id).order_by('-created')
    return render(request, 'todoozer/home.html', {'lists': lists, 'selected_list_id':selected_list_id})

def list(request):
    list = get_object_or_404(TodoList, pk=request.GET['list_id'])
    ordered_list = list.todoitem_set.order_by('-due_date')
    data = {'items': []}
    for item in ordered_list:
        data['items'].append(item.toDictionary())
    print(data)
    return JsonResponse(data)

def new_list(request):
    new_list = TodoList(user=request.user, name=request.GET['list_name'])
    new_list.save()
    return redirect(reverse('todoozer:home') + '?selected_list_id=' + str(new_list.id))

def add(request):
    list_id = TodoList.objects.get(pk=request.POST['list_id']).id
    toto = random.choice(TotoItem.objects.all())
    new_todo = TodoItem(
        list_id = list_id,
        item_text = request.POST['item_text'],
        due_date = request.POST['due_date'],
        urgency = request.POST['urgency'],
        toto_item = toto)
    new_todo.save()
    return redirect(reverse('todoozer:home') + '?selected_list_id=' + str(list_id))

def remove(request):
    list_id = TodoList.objects.get(pk=request.POST['list_id'])
    item_id = request.POST('todoitem_id')
    TodoItem.objects.filter(id=item_id).delete()
    return redirect(reverse('todoozer:list', args=(list_id,)))


