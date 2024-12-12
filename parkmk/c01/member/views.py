from django.shortcuts import render, redirect
from member.models import Member
from django.http import JsonResponse

# Create your views here.
def login(request):
  # GET 요청: 쿠키에서 ID를 가져오고 로그인 페이지 렌더링
  cookId = request.COOKIES.get('cookId', '')  # 쿠키에서 cookId 가져오기
  context = {'cookId': cookId}
  return render(request, 'login.html', context)

# 로그인 POST
def loginChk(request):
  # POST 요청: 로그인 처리
  m_id = request.POST.get('m_id', '')  # ID 필드
  m_password = request.POST.get('m_password', '')  # 비밀번호 필드
  saveId = request.POST.get('saveId',"")  # ID 저장 여부
  print(m_id, m_password, saveId)
  # 데이터베이스 확인
  qs = Member.objects.filter(m_id=m_id, m_password=m_password)
  
  print(qs)
  if qs:
    # 로그인 성공: 세션 추가 및 응답 생성
    request.session['session_m_id'] = qs[0].m_id
    request.session['session_m_nickName'] = qs[0].m_nickName
    request.session['session_m_auth'] = qs[0].m_auth
    
    # 쿠키 처리
    response = JsonResponse({"result": "success", "member": list(qs.values())})
    if saveId == "1":
      response.set_cookie('cookId', m_id, max_age=60*60)  # 쿠키에 ID 저장
    else:
      response.delete_cookie('cookId')
  else:
    # 로그인 실패
    response = JsonResponse({"result": "fail"})
  print(response)
  return response



## 로그아웃
def logout(request):
  request.session.clear()
  # request.COOKIES.clear()
  return redirect("/")