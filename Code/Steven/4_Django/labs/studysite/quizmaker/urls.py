from django.urls import path
from . import views

app_name = 'quizmaker'

urlpatterns = [
    path('', views.index, name='index'),
    path('import_text', views.import_text, name='import text')

]

