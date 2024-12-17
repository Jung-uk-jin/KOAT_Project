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

def kakao_pay_request(request):
    if request.method == "POST":
        product_name = request.POST.get("p_name")
        product_price = request.POST.get("p_price")

        headers = {
            "Authorization": f"KakaoAK {KAKAOPAY_API_KEY}",
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
        }

        data = {
            "cid": "TC0ONETIME",
            "partner_order_id": "order1234",
            "partner_user_id": "user1234",
            "item_name": product_name,
            "quantity": "1",
            "total_amount": int(product_price),
            "tax_free_amount": "0",
            "approval_url": "http://127.0.0.1:8000/package/kakao_pay_approve/",
            "cancel_url": "http://127.0.0.1:8000/package/kakao_pay_cancel/",
            "fail_url": "http://127.0.0.1:8000/package/kakao_pay_fail/",
           # "approval_url": "https://0d0d-203-234-214-81.ngrok-free.app/package/kakao_pay_approve/",
           # "cancel_url": "https://0d0d-203-234-214-81.ngrok-free.app/package/kakao_pay_cancel/",
           # "fail_url": "https://0d0d-203-234-214-81.ngrok-free.app/package/kakao_pay_fail/",

        }

        response = requests.post("https://kapi.kakao.com/v1/payment/ready", headers=headers, data=data)
        response_data = response.json()
        print("response_data:", response_data) 
        if response.status_code == 200:
            # tid 값을 세션에 저장
            request.session['tid'] = response_data['tid']
            return redirect(response_data['next_redirect_pc_url'])
        else:
            return JsonResponse(response_data, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)


# 결제 승인 처리
def kakao_pay_approve(request):
    pg_token = request.GET.get('pg_token')  # 승인 요청 토큰
    tid = request.session.get('tid')       # 세션에서 tid 가져오기

    if not tid:
        return JsonResponse({"error": "Transaction ID (tid) is missing"}, status=400)

    headers = {
        "Authorization": f"KakaoAK {KAKAOPAY_API_KEY}",
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
    }

    data = {
        "cid": "TC0ONETIME",
        "tid": tid,             # 준비 단계에서 저장된 tid
        "partner_order_id": "order1234",
        "partner_user_id": "user1234",
        "pg_token": pg_token,
    }

    response = requests.post("https://kapi.kakao.com/v1/payment/approve", headers=headers, data=data)
    response_data = response.json()
    print("응답 데이터", response_data)  # 응답 내용 확인
    request.session['tid'] = response_data['tid']
    print("세션에 저장된 tid", request.session.get('tid'))

    if response.status_code == 200:
        # 결제 승인 성공 후 결제 완료 페이지로 리디렉션
        return redirect('package:kakao_pay_success')  # 결제 성공 페이지로 리디렉션
    else:
        return JsonResponse(response_data, status=400)
def kakao_pay_success(request):
    # 결제 완료 후 사용자에게 표시할 정보를 제공
    return render(request, 'success.html')  # 결제 완료 페이지


# 결제 취소 처리
def kakao_pay_cancel(request):
    return render(request, 'cancel.html')

# 결제 실패 처리
def kakao_pay_fail(request):
    return render(request, 'fail.html')
