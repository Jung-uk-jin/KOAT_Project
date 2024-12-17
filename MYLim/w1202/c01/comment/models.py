from django.db import models
from member.models import Member
from board.models import Board


# Create your models here.
class Comment(models.Model):
  c_no = models.AutoField(primary_key=True)
  member = models.ForeignKey(Member,on_delete=models.DO_NOTHING)
  board = models.ForeignKey(Board,on_delete=models.CASCADE)
  c_pw = models.CharField(max_length=10, null=True, blank=True)
  c_content = models.TextField()
  c_date = models.DateTimeField(auto_now=True)
  parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
  
  def __str__(self):
    return f"{self.c_no},{self.c_content},{self.c_date}"