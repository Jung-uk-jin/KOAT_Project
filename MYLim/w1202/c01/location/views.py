from django.shortcuts import render
from location.models import Location_inform
from location.models import Attraction
from member.models import Member
from django.http import JsonResponse
from location.models import Location
from location.models import Location1

def location(request):
   qs = Location.objects.all()
   qx = Location1.objects.all()
   context = {'llist':qs, '1list':qx}
   return render(request,'location.html',context)

def up(request, lo_name):
    m_id = request.session.get('session_m_id')
    qs = Attraction.objects.filter(a_location__l_location=lo_name)
    qx = Location_inform.objects.filter(l_location=lo_name)
    qv = Location_inform.objects.get(l_location=lo_name)

    # count = qv.l_like_members.count()
    # # 좋아요 상태를 확인
    # if qv.l_like_members.filter(pk=m_id).exists():
    #     result = '1'
    #     count = qv.l_like_members.count()
    # else:
    #     result = '0'
    context = {'informs': qs, 'location':qx, 'location2':qv, 
              #  'result':result, 'count':count
               }
    return render(request, 'up.html', context)

# def like(request):
#   m_id = request.session["session_m_id"]
#   member = Member.objects.get(m_id=m_id)
#   l_no = request.POST.get("l_no")
#   l_informs = Location_inform.objects.get(l_no=l_no)

#   # 저장 board.b_no, board.member.m_id
#   if l_informs.l_like_members.filter(pk=m_id).exists(): # 좋아요클릭한 상태
#     l_informs.l_like_members.remove(member)
#     result = "remove" # 좋아요취소
#   else:
#     l_informs.l_like_members.add(member)
#     result = "add"    # 좋아요추가  
  
#   context = {"result":result,"count":l_informs.l_like_members.count()}
  
#   return JsonResponse(context)