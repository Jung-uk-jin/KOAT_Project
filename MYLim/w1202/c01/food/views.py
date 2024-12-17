from django.shortcuts import render
from food.models import Food_inform
from food.models import Store
from food.models import Eat
def eat(request):
  qc = Eat.objects.all()
  context={'flist':qc}
  return render(request,'eat.html',context)

def niku(request,e_name):
  qs = Store.objects.filter(s_foodname__f_name=e_name)
  qx = Food_inform.objects.filter(f_name=e_name)
  context = {'informs' : qs,'location':qx}
  return render(request,'niku.html',context)