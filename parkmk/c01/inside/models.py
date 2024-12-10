from django.db import models
from member.models import Member
from datetime import datetime

class Location_inform(models.Model):
  l_no = models.AutoField(primary_key=True)
  l_member = models.ForeignKey(Member,on_delete = models.DO_NOTHING,null=True)
  l_location = models.CharField(max_length=30)
  l_description = models.TextField(null=True)
  l_description2 = models.CharField(max_length=3000, default="Default Description")
  l_name =models.CharField(max_length=30)
  l_file = models.ImageField(null=True,upload_to='board')

  def __str__(self):
    return f"{self.l_no},{self.l_description2},{self.l_location},{self.l_name}"

class Location(models.Model):
  lo_name = models.CharField(max_length=30, primary_key=True)