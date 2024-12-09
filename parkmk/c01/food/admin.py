from django.contrib import admin
from food.models import Food_inform

@admin.register(Food_inform)
class Food_informAdmin(admin.ModelAdmin):
  list_display = ['f_no','f_name','f_description','f_location']