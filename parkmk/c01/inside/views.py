from django.shortcuts import render
from inside.models import Location_inform
from inside.models import Location

def up(request,lo_name):
    qs = Location_inform.objects.get(l_location=lo_name)

    context = {'informs':qs}
    return render(request, 'up.html',context)