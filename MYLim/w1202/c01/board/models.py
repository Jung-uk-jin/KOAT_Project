from django.db import models
from member.models import Member
from datetime import datetime

class Board(models.Model):
  b_no = models.AutoField(primary_key=True)
  member = models.ForeignKey(Member,on_delete=models.DO_NOTHING, null=True)
  b_like_members = models.ManyToManyField(Member,default='', related_name='like_member')
  b_dislike_members = models.ManyToManyField(Member,default='', related_name='dislike_member')
  b_title = models.CharField(max_length=30)
  b_content = models.TextField()
  b_hit = models.IntegerField(default=0)
  b_header = models.CharField(max_length=10)
  b_date = models.DateTimeField(auto_now=True)
  b_file = models.ImageField(blank=True, null=True,upload_to='board')
  
  def __str__(self):
    return f"{self.b_no},{self.b_title},{self.b_date}"