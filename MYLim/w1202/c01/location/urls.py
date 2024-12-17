from django.urls import path
from . import views

app_name = 'location'
urlpatterns = [
    path('up/<str:lo_name>/',views.up,name='up'),
    # path('like/',views.like,name='like'),
    path('location/',views.location,name='location'),
]