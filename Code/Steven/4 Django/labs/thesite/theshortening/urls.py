

from django.urls import path
from . import views

app_name = 'theshortening'
urlpatterns = [
    path('', views.index, name='index'),
]