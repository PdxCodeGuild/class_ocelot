from django.urls import path

from . import views

from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_todo/', views.add_todo, name='add_todo')
]
