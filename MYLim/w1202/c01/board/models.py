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
  b_header = models.CharField(max_length=10, null=True, blank=True)
  b_date = models.DateTimeField(auto_now=True)
  b_file = models.ManyToManyField('BoardFile', blank=True)  # ManyToManyField로 이미지 여러 개 연결
  
  def __str__(self):
      return f"{self.b_no},{self.b_title},{self.b_date}"

class BoardFile(models.Model):
  b_board = models.ForeignKey(Board, related_name='files', on_delete=models.CASCADE)  # Board와 연결
  b_file = models.ImageField(upload_to='board/', null=True, blank=True)  # 이미지 파일 필드
  
  def __str__(self):
      return f"File for {self.b_board.b_title}"