from django.conf.urls import url
from . import views

publiclibrary = 'publiclibrary'
urlpatterns = [
    path('', views.index, name='index'),

]