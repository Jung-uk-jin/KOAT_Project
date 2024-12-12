
from django.contrib import admin
from django.urls import path,include
app_name=""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('region/',include('region.urls')),
]
