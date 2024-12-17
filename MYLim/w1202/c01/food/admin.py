from django.contrib import admin
from food.models import Food_inform
from food.models import Store
from food.models import Eat

@admin.register(Food_inform)
class Food_informAdmin(admin.ModelAdmin):
  list_display = ['f_no','f_name','f_description']

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
  list_display = ['s_name','s_address','s_number']

@admin.register(Eat)
class EatAdmin(admin.ModelAdmin):
  list_display = ['e_name']