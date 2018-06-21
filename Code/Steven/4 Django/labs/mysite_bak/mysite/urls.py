from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    # path('to     do/', include('todo.urls')),
    path ( 'todo/' , include ( 'todolist.urls' ) ) ,
    path('admin/', admin.site.urls),
]