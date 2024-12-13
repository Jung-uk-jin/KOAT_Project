from django.urls import path
from .views import chatbot_reply
from . import views

app_name='chatbot'
urlpatterns = [
    path('chat/', views.chat_page, name='chat_page'),
    path('reply/', views.chatbot_reply, name='chatbot_reply'),
]