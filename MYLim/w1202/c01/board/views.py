from django.shortcuts import render, redirect
from board.models import Board
from member.models import Member
from comment.models import Comment
from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator # 페이지 넘버링
import os
from django.conf import settings
from django.http import JsonResponse

### 게시판 리스트
def blist(request):
  npage = int(request.GET.get('npage',1))
  qs = Board.objects.all().order_by('-b_no')
  cl = request.GET.get('cl','')
  searchType = request.GET.get('type','b_title')
  
  if cl:
    if searchType == 'b_title':
      qs = Board.objects.filter(b_title__icontains=cl)
    elif searchType == 'b_content':
      qs = Board.objects.filter(b_content__icontains=cl)
    elif searchType == 'b_title_content':
      qs = Board.objects.filter(Q(b_title__icontains=cl)|Q(b_content__icontains=cl))
  
  paginator = Paginator(qs,2)
  blist = paginator.get_page(npage)
  context = {'blist':blist,'npage':npage,'cl':cl,'searchType':searchType}
  return render(request,'blist.html',context)

### 게시판 글쓰기
def bwrite(request):
  if request.method =="GET":
    return render(request,'bwrite.html')
  else:
    m_id = request.session['session_m_id']
    member = Member.objects.get(m_id=m_id)
    b_title=request.POST.get("b_title")
    b_content=request.POST.get("b_content")
    b_file=request.FILES.get("b_file","")
    
    qs = Board.objects.create(member=member,b_title=b_title,b_content=b_content,b_file=b_file)
    qs.save()
  
    context={'wmsg':"1"}
    return render(request, 'bwrite.html',context)

### 게시판 글보기
def bview(request,b_no):
  m_id = request.session.get('session_m_id')
  print('세션아이디 : ',m_id)
  if not m_id:
    # m_id 가 없을경우
    return render(request,'bview.html',{'rq_login': True})
  else:
    member = Member.objects.get(m_id=m_id)
    npage = request.GET.get('npage',1)
    qs = Board.objects.get(b_no=b_no)
    c_qs = Comment.objects.filter(board=qs).order_by('c_no')
    
    ## 이전글, 다음글
    prev_qs = Board.objects.filter(b_no__lt=qs.b_no).order_by('-b_no').first()
    next_qs = Board.objects.filter(b_no__gt=qs.b_no).order_by('b_no').first()
    
    count = f"좋아요 {qs.b_like_members.count()}"
    # 좋아요 상태를 확인
    if qs.b_like_members.filter(pk=m_id).exists():
      result = '1'
      print("좋아요 상태: 클릭됨")
      count = f"좋아요 {qs.b_like_members.count()}"
    else:
      result = '0'
      print("좋아요 상태: 클릭되지 않음")

    dis_count = f"싫어요 {qs.b_dislike_members.count()}"
    # 싫어요 상태를 확인
    if qs.b_dislike_members.filter(pk=m_id).exists():
      dis_result = '1'
      print("싫어요 상태: 클릭됨")
      dis_count = f"싫어요 {qs.b_dislike_members.count()}"
    else:
      dis_result = '0'
      print("싫어요 상태: 클릭되지 않음")
    
    ## 조회수 증가 방지, 날짜 설정 (쿠키기간)
    day1 = datetime.replace(datetime.now(),hour=23,minute=59,second=59)
    expires = datetime.strftime(day1,'%a, %d-%b-%Y %H:%M:%S GMT')
    print('날짜 : ',expires)
    context = {'board':qs, 'prev_board':prev_qs, 'next_board':next_qs,
               'npage':npage, 'clist':c_qs, 'result': result, 'count':count,
               'dis_result':dis_result, 'dis_count':dis_count}
    response = render(request,'bview.html',context)
    ## 쿠키확인
    if request.COOKIES.get('cookie_boardNo') is not None:
      cookies = request.COOKIES.get('cookie_boardNo') # 1|5|6|2
      cookies_list = cookies.split('|')
      if str(b_no) not in cookies_list:
        response.set_cookie('cookie_boardNo',cookies+f"|{b_no}",expires=expires)
        # 조회수 1증가
        qs.b_hit += 1
        qs.save() 
    else:
      # 쿠키저장
      response.set_cookie('cookie_boardNo',b_no,expires=expires) # 쿠키에 bno 저장 / 기간 expires
      # 조회수 1증가
      qs.b_hit += 1
      qs.save()
      
    return response

### 게시판 글 수정
def bupdate(request,b_no):
  if request.method == 'GET':
    qs = Board.objects.get(b_no=b_no)
    context = {'board':qs}
    return render(request,'bupdate.html',context)
  else:
    b_no = request.POST.get('b_no')
    b_title = request.POST.get('b_title')
    b_content = request.POST.get('b_content')
    b_file = request.FILES.get('b_file')
    delete_image = request.POST.get('delete_image')
    qs = Board.objects.get(b_no=b_no)
    
    if delete_image:  # 이미지 삭제 체크박스가 체크되었을 경우
      if qs.b_file:
        image_path = os.path.join(settings.MEDIA_ROOT, qs.b_file.name)
        if os.path.exists(image_path):  # 파일이 존재하면 삭제
          os.remove(image_path)
          qs.b_file = None  # 초기화
      
    qs.b_title = b_title
    qs.b_content = b_content
    if b_file:
      qs.b_file=b_file
    qs.save()
    context = {'umsg':b_no}
    return render(request,'bupdate.html',context)

### 게시판 글 삭제
def bdelete(request,b_no):
  Board.objects.get(b_no=b_no).delete()
  context = {'dmsg':b_no}
  return render(request,'blist.html',context)

### 좋아요
def likes(request):
  m_id = request.session["session_m_id"]
  member = Member.objects.get(m_id=m_id)
  b_no = request.POST.get("b_no")
  board = Board.objects.get(b_no=b_no)

  if board.b_dislike_members.filter(pk=m_id).exists(): # 싫어요클릭한 상태
    board.b_dislike_members.remove(member)
  
  # 저장 board.b_no, board.member.m_id
  if board.b_like_members.filter(pk=m_id).exists(): # 좋아요클릭한 상태
    board.b_like_members.remove(member)
    result = "remove" # 좋아요취소
  else:
    board.b_like_members.add(member)
    result = "add"    # 좋아요추가  
  
  print("좋아요 개수 확인 : ",board.b_like_members.count())
  context = {"result":result,"count":board.b_like_members.count(), "dis_count":board.b_dislike_members.count()}
  
  return JsonResponse(context)

### 싫어요
def dislikes(request):
  m_id = request.session["session_m_id"]
  member = Member.objects.get(m_id=m_id)
  b_no = request.POST.get("b_no")
  board = Board.objects.get(b_no=b_no)

  if board.b_like_members.filter(pk=m_id).exists(): # 좋아요클릭한 상태
    board.b_like_members.remove(member)
    
  # 저장 board.b_no, board.member.m_id
  if board.b_dislike_members.filter(pk=m_id).exists(): # 싫어요클릭한 상태
    board.b_dislike_members.remove(member)
    result = "remove" # 싫어요취소
  else:
    board.b_dislike_members.add(member)
    result = "add"    # 싫어요추가  
    
  
  
  print("싫어요 개수 확인 : ",board.b_dislike_members.count())
  context = {"dis_result":result, "count":board.b_like_members.count(), "dis_count":board.b_dislike_members.count()}
  
  return JsonResponse(context)