from django.urls import path
from . import views

app_name = 'package'
urlpatterns = [
    path('plist/',views.plist,name='plist'),
]
