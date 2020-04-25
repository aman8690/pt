from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=50)
    DOB = models.CharField(max_length=10)
    Mob_no = models.CharField(max_length=10)
    Email_id = models.CharField(max_length=20)

class test(models.Model):
    ques = models.TextField(max_length=100)
    marks = models.CharField

class institute(models.Model):
    name = models.TextField(max_length=50)
    Email_id = models.CharField(max_length=20)
    Mob_no = models.CharField(max_length=10)
    pincode = models.CharField(max_length=6)
