# from django.conf.urls import url (this is from quickstart - did not work)
from django.urls import path
from . import views

app_name = 'theshortening'
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('save_url', views.save_url, name='save_url'),
    path('repointer', views.repointer, name='repointer'),

]

# path ( 'index/' , views.index )  # template containing input field and button and form and list
# path ( 'redirect/<str:code>/' , views.redirect )  # directing
