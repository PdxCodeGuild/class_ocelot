# from django.conf.urls import url # note: this line is from quickstart - did not work)
from django.urls import path
from . import views

app_name = 'theshortening'
urlpatterns = [
    path('', views.index, name='index'),
    path('save_url', views.save_url, name='save_url'),
    path('<str:code>/', views.redeem_shortcode, name='redeem_shortcode'),
]

# path ( 'index/' , views.index )  # template containing input field and button and form and list
# path ( 'redirect/<str:code>/' , views.redirect )  # directing
