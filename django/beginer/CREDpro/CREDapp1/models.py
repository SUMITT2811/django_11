from django.db import models

class Shoes(models.Model):
    sId=models.AutoField(primary_key=True)
    sName=models.CharField(max_length=100)
    sBrand=models.CharField(max_length=100)
    size=models.IntegerField()
    sType=models.CharField(max_length=100)
    price=models.FloatField(default=0.0)
    STATUS_CHOICES =[
        ('MEN','men'),
        ('WOMEN','women'),
        ('KIDS','kids'),
    ]
    status = models.CharField(max_length=10, choices = STATUS_CHOICES , default = 'active')

