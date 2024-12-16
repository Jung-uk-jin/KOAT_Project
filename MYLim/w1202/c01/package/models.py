from django.db import models

# Create your models here.
class Package(models.Model):
  p_no = models.AutoField(primary_key=True)
  p_name = models.CharField(max_length=100)
  p_price = models.IntegerField()
  p_file = models.ImageField(null=True)

  def __str__(self):
    return f"{self.p_no}. {self.p_name}, {self.p_price}"