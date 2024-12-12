from django.shortcuts import render
from inside.models import Location
from inside.models import Location1

def index(request):
  qs = Location.objects.all()
  qx = Location1.objects.all()
  
  context = {'llist' : qs,'1list': qx}
  return render(request,'index.html', context)