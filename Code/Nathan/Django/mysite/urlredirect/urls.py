from django.urls import path

from . import views

from django.urls import path

from . import views

app_name = 'urlredirect'

urlpatterns = [
    path('', views.index, name='index'),
    path('save_shortener/', views.save_shortener, name='save_shortener'),
    path('redirect_form/', views.redirect_form, name='redirect_form'),
    path('<str:code>/', views.short_url_redirect, name='short_url_redirect'),
]
