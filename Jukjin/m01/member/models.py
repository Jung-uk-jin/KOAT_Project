from django.db import models
from datetime import datetime

class Member(models.Model):
  m_username = models.CharField(max_length=10)
  m_id = models.CharField(max_length=10,primary_key=True)
  m_password = models.CharField(max_length=20)
  m_nickName = models.CharField(max_length=15)
  m_gender = models.CharField(max_length=5)
  m_date = models.DateField(auto_now=True)
  m_auth = models.IntegerField(default=1)

  def __str__(self):
    return f"{self.m_id},{self.m_username},{self.m_date}"
