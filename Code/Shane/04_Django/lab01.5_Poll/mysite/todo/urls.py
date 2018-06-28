from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [

    path('', views.index, name='index'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('mylogin/', views.mylogin, name='mylogin'),
    path('register/', views.register, name='register'),
    path('mylogout/', views.mylogout, name='mylogout'),

]
