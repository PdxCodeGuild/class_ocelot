from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('home/', views.home, name='home'),
    path('filter_title/', views.filter_title, name='filter_title'),
    path('filter_author/', views.filter_author, name='filter_author'),
    path('checkout/', views.checkout, name='checkout'),
]



