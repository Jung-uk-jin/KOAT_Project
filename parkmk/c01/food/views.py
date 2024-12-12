from django.shortcuts import render
from food.models import Food_inform
from food.models import Store

def eat(request):
  return render(request,'eat.html')

def niku(request,e_name):
  qs = Store.objects.filter(f_name=e_name)
  qx = Food_inform.objects.filter(f_name=e_name)

  context = {'informs' : qs,'location':qx}
  return render(request,'niku.html',context)
