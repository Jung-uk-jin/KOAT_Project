from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from django.core import serializers # json타입
from member.models import Member
import random # 랜덤 비밀번호

# 이메일 발송 관련
import smtplib
from email.mime.text import MIMEText


# 회원가입(약관동의)
def sigup01(request):
  return render(request, 'sigup01.html')

# 회원가입(정보입력)
def sigup02(request):
  return render(request, 'sigup02.html')

# 아이디 중복 확인
def idchk(request):
  m_id = request.POST.get("m_id","")
  qs = Member.objects.filter(m_id=m_id)

  print(m_id)
  print(qs)

  if qs:
    context = {"result":"success"}
  else:
    context = {"result":"fail"}
  return JsonResponse(context)


# 회원가입(정보 저장)
def signcp(request):
  if request.method == "POST":
    id = request.POST.get('아이디')
    pw = request.POST.get('비밀번호')
    name = request.POST.get('실명')
    nicName = request.POST.get('별명')
    gender = request.POST.get('gender')
    email = request.POST.get('이메일')
    print("변수", id, pw, name, nicName, gender, email)
    Member.objects.create(m_id=id, m_password=pw, m_username=name, m_nickName=nicName, m_gender=gender, m_email=email)  # 여기 주석 해제하면 정보 DB에 저장됨
    return redirect("member:sigcomp")
  else:  
    return render(request, 'signup02.html')

# 가입완료 
def sigcomp(request):
  return render(request, "sigcomp.html")


# 로그인 GET
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


# 아이디 찾기
def srchid(request):
  if request.method == "GET":
    return render(request, 'srchid.html')
  else:   #POST
    m_username = request.POST.get('m_username','')
    m_email = request.POST.get('m_email','')
    print(m_username, m_email)
    qs = Member.objects.get(m_username=m_username)
    print(qs)
    if qs:
      response = JsonResponse({"result": "success", "id":qs.m_id})
    else:
      response = JsonResponse({"result": "flase"})
    print(qs.m_id)
    print(response)
    return response



# 비밀번호 찾기
def srchpw(request):
  if request.method == "GET":
    return render(request, 'srchpw.html')
  else:   # POST
    m_id = request.POST.get('m_id','')
    m_username = request.POST.get('m_username','')
    m_email = request.POST.get('m_email','')
    print(m_id , m_username, m_email)
    # 이메일 기본 설정
    smtpName = "smtp.naver.com"
    smtpPort = 587
  
    qs = Member.objects.get(m_id=m_id, m_username=m_username, m_email=m_email)
    print(qs)
    if qs:
    # 회원정보 확인 시 작성 시작
    # 자신의 네이버메일주소,id, pw, 받는사람이메일주소
      sendEmail = "tjdwkwnsla1@naver.com"         
      emailPw = "RJKDFMZCJLW4"
      recvEmail = m_email

    # 1. 임시 비밀번호 생성
      # 비밀번호 길이 설정
      password_length = 10
      # 랜덤 비밀번호 생성
      random_password = ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*") for _ in range(password_length))
      print("Random Password: ", random_password)

      # 2. 메일 발송
      title = "임시 비밀번호 입니다"
      content = f"""\
        KOAT에서 임시 비밀번호를 보내드립니다.
        {random_password}
        해당 번호로 로그인하시면 됩니다.
        """
      msg = MIMEText(content)
      msg['Subject'] = title
      msg['From'] = sendEmail
      msg['To'] = recvEmail

      s = smtplib.SMTP(smtpName,smtpPort)
      s.starttls()
      s.login(sendEmail,emailPw)
      s.sendmail(sendEmail,recvEmail,msg.as_string())
      s.quit()
      print("메일 발송 완료")

      # de에 임시 비번 저장
      qs.m_password = random_password
      qs.save()

      response = JsonResponse({"result": "success"})
    else:
      response = JsonResponse({"result": "flase"})

    return response

# 회원정보 보기 페이지
def meminfo(request):
  m_id = request.session['session_m_id']
  print('아이디 : ',m_id)
  qs = Member.objects.filter(m_id=m_id)
  print(qs)
  context = {"mem":qs[0]}
  return render(request, 'meminfo.html', context)

# 회원정보 수정 페이지
def memupd(request):
  m_id = request.session['session_m_id']
  print('아이디 : ',m_id)
  qs = Member.objects.filter(m_id=m_id)
  print(qs)
  context = {"mem":qs[0]}
  return render(request, 'memupd.html', context)

# 회원 정보 수정 저장
def infoupd(request):
  id = request.POST.get('아이디')
  pw = request.POST.get('비밀번호')
  name = request.POST.get('실명')
  nickName = request.POST.get('별명')
  gender = request.POST.get('gender')
  email = request.POST.get('이메일')
  print("변수", id, pw, name, nickName, gender, email)

  qs = Member.objects.get(m_id=id)
  qs.m_password = pw
  qs.m_username = name
  qs.m_nickName = nickName
  qs.m_gender = gender
  qs.m_email = email
  qs.save()


  # Member.objects.create(m_id=id, m_password=pw, m_username=name, m_nickName=nicName, m_gender=gender, m_email=email)  # 여기 주석 해제하면 정보 DB에 저장됨
  return redirect("member:meminfo")





# # 회원 리스트 (관리자)  // 안함
# def mlist(request):
#   id = request.session['session_id']
#   if id == 'admin':
#     qs = Member.objects.all()
#   else:
#     qs = Member.objects.filter(id=id)
#   context = {"mlist":qs}
#   return render(request, 'mlist.html', context)