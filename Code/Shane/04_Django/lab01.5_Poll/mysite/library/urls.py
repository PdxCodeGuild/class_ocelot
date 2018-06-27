from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [

    path('', views.index, name='index'),
    path('author', views.index, name='author'),
    path('book', views.index, name='book'),

]
