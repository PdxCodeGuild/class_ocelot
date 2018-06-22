from django.urls import path

from . import views

app_name = 'short_url'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('add_url/', views.add_url, name='add_url'),
    path('<str:url_code>/', views.short_code, name='url_code'),
]
