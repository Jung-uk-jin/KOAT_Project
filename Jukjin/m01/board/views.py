from django.shortcuts import render, redirect
from board.models import Board
from member.models import Member
from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator # 페이지 넘버링

# 게시판
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


# 게시글 작성
def bwrite(request):
  if request.method =="GET":
    return render(request,'bwrite.html')
  else:
    # id = 'aaa'
    # member = Member.objects.filter(id=id)
    b_title=request.POST.get("b_title")
    b_content=request.POST.get("b_content")
    b_file=request.FILES.get("b_file","")
    print("파일정보 : ",b_file)
    qs = Board.objects.create(b_title=b_title,b_content=b_content,b_file=b_file)
  
    context={'wmsg':"1"}
    return render(request, 'bwrite.html',context)
  
# 게시글상세보기
def bview(request,b_no):
  npage = request.GET.get('npage',1)
  qs = Board.objects.get(b_no=b_no)
  
  ## 이전글, 다음글
  prev_qs = Board.objects.filter(b_no__lt=qs.b_no).order_by('-b_no').first()
  next_qs = Board.objects.filter(b_no__gt=qs.b_no).order_by('b_no').first()
  
  ## 조회수 증가 방지, 날짜 설정 (쿠키기간)
  day1 = datetime.replace(datetime.now(),hour=23,minute=59,second=59)
  expires = datetime.strftime(day1,'%a, %d-%b-%Y %H:%M:%S GMT')
  print('날짜 : ',expires)
  context = {'board':qs, 'prev_board':prev_qs, 'next_board':next_qs, 'npage':npage}
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

# 게시글 수정
def bupdate(request,b_no):
  if request.method =="GET":
    qs=Board.objects.get(b_no=b_no)
    context={"board":qs}
    return render(request,'bupdate.html',context)
  else:
    b_no=request.POST.get("b_no")
    b_title=request.POST.get("b_title")
    b_content=request.POST.get("b_content")
    b_file=request.FILES.get("b_file","")
    print("파일정보 : ",b_file)
    # 글쓰기 수정 저장
    qs=Board.objects.get(b_no=b_no)
    qs.b_title = b_title
    qs.b_content = b_content
    if b_file:
      qs.b_file=b_file
    qs.save()

    context={'umsg':b_no}
    return render(request, 'bupdate.html',context)