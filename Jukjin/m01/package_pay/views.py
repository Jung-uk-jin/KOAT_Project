from django.shortcuts import render
from package_pay.models import Package_infrom
# Create your views here.
def payment(request):
  qs = Package_infrom.objects.all()
  context = {'plist' : qs}
  return render(request,'payment.html',context)