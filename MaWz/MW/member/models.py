from django.db import models
# import datetime
from datetime import datetime

class Member(models.Model):
  m_id = models.CharField(max_length=50,primary_key=True)
  m_password = models.CharField(max_length=100)
  m_username = models.CharField(max_length=100)
  m_nickName = models.CharField(max_length=100)
  m_gender = models.CharField(max_length=10, default='남자')
  m_email = models.CharField(max_length=100)
  m_date = models.DateTimeField(auto_now=True)
  m_auth = models.IntegerField(default=1)
  
  def __str__(self):
    return f"{self.m_id},{self.m_password},{self.m_username},{self.m_nickName},{self.m_gender},{self.m_email},{self.m_date},{self.m_auth},"
