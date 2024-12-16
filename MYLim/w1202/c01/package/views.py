import json
import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from package.models import Package

# 카카오페이 결제 요청 URL
KAKAOPAY_URL = "https://kapi.kakao.com/v1/payment/ready"
KAKAOPAY_APPROVE_URL = "https://kapi.kakao.com/v1/payment/approve"

# 카카오페이 API 키
KAKAOPAY_API_KEY = settings.KAKAOPAY_API_KEY  # settings.py에서 설정한 카카오페이 API 키

def plist(request):
    qs = Package.objects.all
    context = {"plist":qs}
    return render(request, 'plist.html',context)

# 결제 요청 처리
def plist(request):
    # 모든 상품 리스트를 가져옵니다.
    qs = Package.objects.all()
    context = {"plist": qs}
    return render(request, 'plist.html', context)

def kakao_pay_request(request, p_no):
    # 특정 상품(p_no)을 가져옵니다.
    package = get_object_or_404(Package, p_no=p_no)

    # 카카오페이 결제 요청 데이터 구성
    headers = {
        "Authorization": f"KakaoAK {KAKAOPAY_API_KEY}",  # REST API 키
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    }

    data = {
        "cid": "TC0ONETIME",  # 테스트용 CID
        "partner_order_id": f"order_{package.p_no}",  # 상품 고유 번호
        "partner_user_id": "user1234",  # 임의 사용자 ID
        "item_name": package.p_name,  # 상품 이름
        "quantity": 1,
        "total_amount": package.p_price,  # 상품 가격
        "tax_free_amount": 0,
        "approval_url": "http://localhost:8000/kakao_pay_approve/",
        "cancel_url": "http://localhost:8000/kakao_pay_cancel/",
        "fail_url": "http://localhost:8000/kakao_pay_fail/",
    }

    response = requests.post("https://kapi.kakao.com/v1/payment/ready", headers=headers, data=data)
    response_data = response.json()

    if response.status_code == 200:
        # 결제 페이지로 리디렉션
        return redirect(response_data['next_redirect_pc_url'])
    else:
        # 오류 메시지를 반환
        return JsonResponse(response_data, status=400)

# 결제 승인 처리
def kakao_pay_approve(request):
    pg_token = request.GET.get("pg_token")

    headers = {
        "Authorization": f"KakaoAK {KAKAOPAY_API_KEY}",
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    }

    data = {
        "cid": "TCS0000004",  # 상점 ID
        "tid": request.GET.get("tid"),  # 결제 요청 시 받은 tid
        "partner_order_id": "order1234",  # 주문 ID
        "partner_user_id": "user1234",  # 사용자 ID
        "pg_token": pg_token,
    }

    response = requests.post(KAKAOPAY_APPROVE_URL, headers=headers, data=data)
    response_data = response.json()

    if response.status_code == 200:
        # 결제 승인 성공
        return render(request, 'success.html', {"response": response_data})
    else:
        return JsonResponse(response_data, status=400)

# 결제 취소 처리
def kakao_pay_cancel(request):
    return render(request, 'cancel.html')

# 결제 실패 처리
def kakao_pay_fail(request):
    return render(request, 'fail.html')
