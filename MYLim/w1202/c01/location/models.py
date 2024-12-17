from django.db import models
from member.models import Member
from datetime import datetime


class Location_inform(models.Model):
  l_no = models.AutoField(primary_key=True)
  l_location = models.CharField(max_length=30)
  l_description = models.TextField(null=True)
  # l_like_members = models.ManyToManyField(Member,default='', related_name='location_like_member')
  l_subtitle = models.CharField(max_length=50, null=True)
  l_file = models.ImageField(null=True,upload_to='board/')
  
  def __str__(self):
    return f"{self.l_no},{self.l_location}"

class Location(models.Model):
  lo_name = models.CharField(max_length=30, primary_key=True)

class Location1(models.Model):
  lo_name = models.CharField(max_length=30, primary_key=True)

class Attraction(models.Model):
  a_location = models.ForeignKey(Location_inform, on_delete = models.CASCADE, null=True)
  a_name = models.CharField(max_length=30, primary_key=True)
  a_description = models.TextField(null=True)
  a_file = models.ImageField(null=True,upload_to='board/')