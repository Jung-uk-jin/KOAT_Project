from django.shortcuts import render
from member.models import Member

# Create your views here.
def index(request):
  return render(request,'index.html')