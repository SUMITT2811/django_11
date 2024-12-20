from django.db import models

class Employee(models.Model):
    empName=models.CharField(max_length=100)
    empSalary=models.FloatField(default=0.0)
    desig=models.CharField(max_length=100)
