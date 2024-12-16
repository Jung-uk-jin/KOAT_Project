from django.contrib import admin
from package.models import Package
# Register your models here.

@admin.register(Package)
class Package_infromAdmin(admin.ModelAdmin):
  list_display=['p_no','p_name','p_price']