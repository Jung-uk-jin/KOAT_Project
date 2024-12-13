from django.contrib import admin
from package_pay.models import Package_infrom
# Register your models here.

@admin.register(Package_infrom)
class Package_infromAdmin(admin.ModelAdmin):
  list_display=['p_no','p_name','p_price']