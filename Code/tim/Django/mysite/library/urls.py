from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('home', views.home, name='home'),
    path('filter', views.filter, name='filter'),
    path('checkout', views.checkout, name='checkout'),
]



