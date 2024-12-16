from django.shortcuts import render

# Create your views here.
def plist(request):
  return render(request,'plist.html')