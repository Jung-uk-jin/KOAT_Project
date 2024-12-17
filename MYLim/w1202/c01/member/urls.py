from django.urls import path,include
from . import views

app_name = "member"
urlpatterns = [
    path('login/', views.login,name="login"),           #  로그인   (로그인 페이지)
    path('loginChk/', views.loginChk,name="loginChk"),  #  로그인   (입력한 정보 체크, 세션, 쿠키 저장)
    path('logout/', views.logout,name="logout"),        #  로그아웃 (세션 삭제)

    path('sigup01/', views.sigup01,name="signup01"),    #  회원가입 (약관동의 페이지)
    path('sigup02/', views.sigup02,name="signup02"),    #  회원가입 (정보입력 페이지)
    path('idchk/', views.idchk,name="idchk"),           #  회원가입 (아이디 중복 체크)
    path('signcp/', views.signcp,name="signcp"),        #  회원가입 (입력한 정보 DB 저장)
    path('sigcomp/', views.sigcomp,name="sigcomp"),     #  회원가입 (회원가입 완료 페이지)

    path('srchid/', views.srchid,name="srchid"),        #  아이디 찾기 (아이디 찾기 페이지)
    path('srchpw/', views.srchpw,name="srchpw"),        #  비밀번호 찾기 (비밀번호 찾기 페이지)
    
    path('meminfo/', views.meminfo,name="meminfo"),     #  회원정보 (내정보) 보기 (회원 정보 보기 페이지)
    path('memupd/', views.memupd,name="memupd"),        #  회원정보 (내정보) 수정 (회원 정보 수정 페이지)
    path('infoupd/', views.infoupd,name="infoupd"),     #  회원정보 (내정보) 수정 (회원 수정 정보 저장 )
]