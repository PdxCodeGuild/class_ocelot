from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:list_id>/', views.list, name='list'),
    path('<int:list_id>/add/', views.add, name='add')
]