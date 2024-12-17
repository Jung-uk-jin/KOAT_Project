from django.urls import path,include
from . import views

app_name = 'food'
urlpatterns = [
    path('eat/',views.eat,name='eat'),
    path('niku/<str:e_name>/',views.niku,name='niku'),

]