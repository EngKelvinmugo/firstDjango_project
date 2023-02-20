from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=15)
    password=models.CharField(max_length=10)
