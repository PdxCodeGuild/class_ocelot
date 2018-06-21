
from django.urls import path
from . import views

app_name = 'todoajax'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_todo', views.add_todo, name='add_todo'),
    path('get_todos', views.get_todos, name='get_todos')
]

