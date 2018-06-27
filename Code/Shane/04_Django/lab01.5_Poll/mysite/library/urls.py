from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [

    path('', views.index, name='index'),
    path('changed/', views.add_book_and_author, name='add_book_and_author'),
]
