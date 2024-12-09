from django.shortcuts import render
from inside.models import Location

def index(request):
  qs = Location.objects.all()
  
  context = {'llist' : qs}
  return render(request,'index.html', context)