from django.shortcuts import render, reverse

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required


def login_register(request):
    next = request.GET.get('next', '')
    return render(request, 'userapp/login_register.html', {'next': next})


@login_required
def home(request):
    print(request.COOKIES)
    return render(request, 'userapp/home.html', {})


def register(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    user = User.objects.create_user(username, email, password)
    login(request, user)

    return HttpResponseRedirect(reverse('userapp:home'))


def mylogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        if 'next' in request.POST and request.POST['next'] != '':
            return HttpResponseRedirect(request.POST['next'])
        return HttpResponseRedirect(reverse('userapp:home'))
    return HttpResponseRedirect(reverse('userapp:registration_login'))


def mylogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('userapp:login_register'))




