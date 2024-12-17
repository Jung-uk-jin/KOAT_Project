from django.db import models
from member.models import Member
from phonenumber_field.modelfields import PhoneNumberField    # pip install django-phonenumber-field[phonenumbers]   <-- 설치 해야 됨

class Food_inform(models.Model):
  f_no = models.AutoField(primary_key=True)
  f_name = models.CharField(max_length=10)
  # f_like_members = models.ManyToManyField(Member,default='', related_name='food_like_member')
  f_description = models.TextField()
  f_file = models.ImageField(null=True,upload_to='board')

  def __str__(self):
    return f"{self.f_no},{self.f_name},{self.f_description}"
  
class Eat(models.Model):
  e_name = models.CharField(max_length=30, primary_key=True)

class Store(models.Model):
  s_foodname = models.ForeignKey(Food_inform,on_delete= models.CASCADE, null=True)
  s_name = models.CharField(max_length=30, primary_key=True)
  s_address = models.CharField(max_length=100,null=True)
  s_number = PhoneNumberField(null=True, blank=True, region='KR')  # 한국 기준 전화번호
  s_file = models.ImageField(null=True,upload_to='board/')