from django.shortcuts import render
from django.template import TemplateDoesNotExist

def region(request, region_name):
    # 지역 이름에 따라 템플릿 또는 데이터를 선택
    template_name = f"{region_name}.html"
    try:
        return render(request, template_name)
    except TemplateDoesNotExist:
        return render(request, "region/default.html", {"region_name": region_name})
