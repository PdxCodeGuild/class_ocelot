
from django.urls import path
from . import views

app_name = 'userapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('login_register/', views.login_register, name='login_register'),
    path('login/', views.mylogin, name='login'),
    path('logout/', views.mylogout, name='logout'),
    path('register/', views.register, name='register'),
]

