from django.shortcuts import render
from inside.models import Location_inform
from inside.models import Attraction

def up(request, lo_name):
    # l_location 필드를 기준으로 필터링
    qs = Attraction.objects.filter(a_location__l_location=lo_name)
    qx = Location_inform.objects.filter(l_location=lo_name)

    context = {'informs': qs, 'location':qx}
    return render(request, 'up.html', context)
