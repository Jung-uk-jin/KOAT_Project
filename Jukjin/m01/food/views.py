from django.shortcuts import render

def eat(request):
  return render(request,'eat.html')

def niku(request):
  return render(request,'niku.html')
