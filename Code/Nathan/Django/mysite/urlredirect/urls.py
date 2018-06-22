from django.urls import path

from . import views

from django.urls import path

from . import views

app_name = 'urlredirect'

urlpatterns = [
    path('', views.index, name='index'),
    path('save_shortener/', views.save_shortener, name='save_shortener'),
]
