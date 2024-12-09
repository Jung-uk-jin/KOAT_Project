from django.contrib import admin
from inside.models import Location_inform
from inside.models import Location

@admin.register(Location_inform)
class Location_informAdmin(admin.ModelAdmin):
  list_display = ['l_no','l_name','l_description','l_description2','l_location']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
  list_display = ['lo_name']