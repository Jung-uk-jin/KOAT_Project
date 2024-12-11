from django.contrib import admin
from inside.models import Location_inform
from inside.models import Location
from inside.models import Attraction


@admin.register(Location_inform)
class Location_informAdmin(admin.ModelAdmin):
  list_display = ['l_no','l_description','l_location','l_subtitle']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
  list_display = ['lo_name']

@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
  list_display = ['a_name','a_description','a_file']