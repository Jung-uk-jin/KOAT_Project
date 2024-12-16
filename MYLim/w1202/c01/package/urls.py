from django.urls import path
from . import views

app_name = 'package'
urlpatterns = [
    path('plist/',views.plist,name='plist'),
    path('kakao_pay_request/', views.kakao_pay_request, name='kakao_pay_request'),
    path('kakao_pay_approve/', views.kakao_pay_approve, name='kakao_pay_approve'),
    path('kakao_pay_cancel/', views.kakao_pay_cancel, name='kakao_pay_cancel'),
    path('kakao_pay_fail/', views.kakao_pay_fail, name='kakao_pay_fail'),
]
