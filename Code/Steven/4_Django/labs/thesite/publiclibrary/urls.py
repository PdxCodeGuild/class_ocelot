from django.conf.urls import url
from django.urls import path
from . import views

publiclibrary = 'publiclibrary'
urlpatterns = [
    path('', views.index, name='index'),
]