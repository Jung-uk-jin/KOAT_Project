from django.urls import path,include
from . import views

app_name = "shop"
urlpatterns = [
    path('hotels/', views.hotels, name='hotels'),
    path('api/hotels/', views.get_hotel_data, name='get_hotel_data'),
]
