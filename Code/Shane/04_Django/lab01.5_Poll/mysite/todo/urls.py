from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [

    path('', views.index, name='index'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('removed_item/', views.remove_todo, name='todo_remove_unicorn'),
    # path('mylogin/', views.mylogin, name='mylogin'),
    # path('mylogout/', views.mylogout, name='mylogout'),
    # path('register/', views.register, name='register'),
]
