from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('blist/',views.blist,name='blist'),
]