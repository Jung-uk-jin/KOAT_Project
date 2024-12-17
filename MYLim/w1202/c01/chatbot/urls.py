from django.urls import path,include
from . import views

app_name = 'chatbot'
urlpatterns = [
    path('bot/', views.bot, name='bot')

]