from django.urls import path
from . import views

app_name = 'inside'
urlpatterns = [
    path('up/<str:lo_name>/',views.up,name='up'),

]