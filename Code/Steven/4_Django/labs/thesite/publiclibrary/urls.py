from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'publiclibrary'
urlpatterns = [
    path('', views.index, name='index'),
    path('checkout_book/', views.checkout_book, name='checkout_book')
]