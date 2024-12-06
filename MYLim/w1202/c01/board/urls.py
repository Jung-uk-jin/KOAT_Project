from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('blist/',views.blist,name='blist'),
    path('likes/',views.likes,name='likes'),
    path('dislikes/',views.dislikes,name='dislikes'),
    path('bwrite/',views.bwrite,name='bwrite'),
    path('bview/<int:b_no>/',views.bview,name='bview'),
    path('bupdate/<int:b_no>/',views.bupdate,name='bupdate'),
    path('bdelete/<int:b_no>/',views.bdelete,name='bdelete'),
]