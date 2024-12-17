from django.contrib import admin
from board.models import Board
from board.models import BoardFile

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
  list_display = ['b_no','b_title','b_date']
  
@admin.register(BoardFile)
class BoardFileAdmin(admin.ModelAdmin):
  list_display = ['b_file']