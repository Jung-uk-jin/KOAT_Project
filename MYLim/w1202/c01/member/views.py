from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from django.core import serializers # json타입
from member.models import Member

# Create your views here.
def login(request):
  return render(request,'login.html')

def loginChk(request):
  m_id = request.POST.get('m_id','')
  m_password = request.POST.get('m_password','')
  print('확인 : ',m_id,m_password)
  qs = Member.objects.filter(m_id=m_id,m_password=m_password)
  
  if qs:
    request.session['session_m_id'] = qs[0].m_id
    request.session['session_m_nickName'] = qs[0].m_nickName
    list_qs = list(qs.values())
    print('세션 아이디 확인 : ',request.session['session_m_id'])
    context = {'result':'success','member':list_qs}
  else:
    context = {'result':'fail'}
  return JsonResponse(context)

def logout(request):
  request.session.clear()
  return redirect('/')