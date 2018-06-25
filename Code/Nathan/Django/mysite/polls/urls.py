
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:todo_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:todo_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:todo_id>/vote/', views.vote, name='vote'),
]
