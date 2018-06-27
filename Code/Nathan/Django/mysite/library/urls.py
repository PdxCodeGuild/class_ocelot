from django.urls import path

from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    #path('author_lookup', views.author_lookup, name='author_lookup')
]
#        path in url      method in views       where in index this is happeing / which form