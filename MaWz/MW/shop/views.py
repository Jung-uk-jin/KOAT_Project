from django.shortcuts import render
from django.http import JsonResponse
from .web_scrap import scrape_hotel_data
import json

def hotels(request):
  return render(request, 'hotels.html')


def get_hotel_data(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            city_name = body.get('city_name', 'Seoul')
            check_in = body.get('check_in', '2024-12-17')
            check_out = body.get('check_out', '2024-12-30')
            rooms = int(body.get('rooms', 1))
            adults = int(body.get('adults', 2))
            children = int(body.get('children', 0))

            # 웹 스크래핑 함수 호출
            hotel_data = scrape_hotel_data(city_name, check_in, check_out, rooms, adults, children)
            
            return JsonResponse({'status': 'success', 'data': hotel_data}, safe=False)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'POST 요청이 필요합니다.'}, status=405)
