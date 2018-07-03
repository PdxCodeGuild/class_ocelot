from django.urls import path

from . import views

app_name = 'todoozer'
urlpatterns = [
    path('login_register/', views.login_register, name='login_register'),
    path('login', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('list/', views.list, name='list'),
    path('new_list/', views.new_list, name='new_list'),
    path('add/', views.add, name='add'),
    path('remove/', views.remove, name='remove')
]

