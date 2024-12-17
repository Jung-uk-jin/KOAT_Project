from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from django.core import serializers # json타입
from member.models import Member
from board.models import Board
from comment.models import Comment

## 댓글 작성
def cwrite(request):
  m_id = request.session['session_m_id']
  member = Member.objects.get(m_id=m_id)
  b_no = request.POST.get('b_no')
  board = Board.objects.get(b_no=b_no)
  c_pw = request.POST.get('c_pw','')
  c_content = request.POST.get('c_content','')
  
  qs = Comment.objects.create(member=member,board=board,c_pw=c_pw,c_content=c_content)
  list_qs = list(Comment.objects.filter(c_no=qs.c_no).values())
  context = {'result':'success','comment':list_qs}
  return JsonResponse(context)

## 댓글 삭제
def cdelete(request):
  c_no = request.POST.get('c_no')
  Comment.objects.get(c_no=c_no).delete()
  context = {'result':'success'}
  return JsonResponse(context)

## 댓글 수정
def cupdate(request):
  m_id = request.session['session_m_id']
  c_no = request.POST.get('c_no',1)
  c_content = request.POST.get('c_content','')
  
  qs = Comment.objects.get(c_no=c_no)
  qs.c_content = c_content
  qs.save()
  list_qs = list(Comment.objects.filter(c_no=qs.c_no).values())
  context = {'result':'success','comment':list_qs}
  return JsonResponse(context)

def reply(request):
  m_id = request.session['session_m_id']
  member = Member.objects.get(m_id=m_id)
  b_no = request.POST.get('b_no')
  parent_c_no = request.POST.get('parent_c_no')
  c_content = request.POST.get('c_content') # 답글 내용
  
  print(parent_c_no)
  print(c_content)
  
  board = Board.objects.get(b_no=b_no)
  parent_comment = Comment.objects.get(c_no=parent_c_no)
  
  qs = Comment.objects.create(member=member,board=board,c_content=c_content,parent_comment=parent_comment)
  list_qs = list(Comment.objects.filter(c_no=qs.c_no).values())
  context = {'result':'success','comment':list_qs}
  
  return JsonResponse(context)