from django.urls import path
from . import views
app_name="region"
urlpatterns = [
    path('<str:region_name>/', views.region, name='region'),
]
