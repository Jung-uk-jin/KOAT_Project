from django.shortcuts import render
from inside.models import Location_inform
from inside.models import Attraction

def up(request, lo_name):
    qs = Attraction.objects.filter(a_location__l_location=lo_name)
    qx = Location_inform.objects.filter(l_location=lo_name)

    context = {'informs': qs, 'location':qx}
    return render(request, 'up.html', context)
