from django.urls import path
from . import views

app_name = 'quizmaker'

urlpatterns = [
    path('', views.index, name='index'),

]

