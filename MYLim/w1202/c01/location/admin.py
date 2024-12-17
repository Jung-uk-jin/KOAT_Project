from django.contrib import admin
from location.models import Location_inform
from location.models import Location
from location.models import Location1
from location.models import Attraction


@admin.register(Location_inform)
class Location_informAdmin(admin.ModelAdmin):
  list_display = ['l_no','l_description','l_location','l_subtitle']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
  list_display = ['lo_name']
  
@admin.register(Location1)
class Location1Admin(admin.ModelAdmin):
  list_display = ['lo_name']

@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
  list_display = ['a_name','a_description','a_file']