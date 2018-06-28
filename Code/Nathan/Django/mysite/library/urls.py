from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/<int:book_id>/', views.checkout, name='checkout'),
    path('checkin/<int:book_id>/', views.checkin, name='checkin')
]
