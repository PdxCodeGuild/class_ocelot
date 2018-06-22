from django.urls import path
from . import views

app_name = 'shortener'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('saveurl/', views.saveurl, name='saveurl'),
    path('redirect/<str:short_url>', views.redirect, name='redirect'),
]