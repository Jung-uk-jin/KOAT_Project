
from django.urls import path,include
from . import views
app_name='package_pay'
urlpatterns = [
    path('payment/',views.payment,name='payment'),
]
