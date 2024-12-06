from django.urls import path
from . import views

app_name = 'heritage'
urlpatterns = [
    path('culture/',views.culture,name='culture'),

]