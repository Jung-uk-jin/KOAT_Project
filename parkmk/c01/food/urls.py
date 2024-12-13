from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('eat/<str:e_name>/',views.eat,name='eat'),
    path('niku/',views.niku,name='niku'),

]