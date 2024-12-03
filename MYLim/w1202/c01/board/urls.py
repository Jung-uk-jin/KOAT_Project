from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('blist/',views.blist,name='blist'),
    path('bwrite/',views.bwrite,name='bwrite'),
    path('bview/',views.bview,name='bview'),
]