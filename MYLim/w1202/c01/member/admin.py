from django.contrib import admin
from member.models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
  list_display = ['m_id','m_nickName','m_date']