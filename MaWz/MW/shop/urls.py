from django.urls import path,include
from . import views

app_name = "shop"
urlpatterns = [
    path('smain/', views.smain,name="smain"),           #  로그인   (로그인 페이지)
]