from django.db import models
from member.models import Member

class Food_inform(models.Model):
  f_no = models.AutoField(primary_key=True)
  f_member = models.ForeignKey(Member, on_delete=models.DO_NOTHING,null=True)
  f_name = models.CharField(max_length=10)
  f_description = models.TextField()
  f_location = models.CharField(max_length=30)
  f_file = models.ImageField(null=True,upload_to='board')

  def __str__(self):
    return f"{self.f_no},{self.f_name},{self.f_description},{self.f_location}"
