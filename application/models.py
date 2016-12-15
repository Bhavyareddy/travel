from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Login(models.Model):
	First_Name = models.CharField(max_length = 20)
	Last_Name = models.CharField(max_length = 20)
	Email_id = models.EmailField()
	Phone_no = models.IntegerField()
	Address = models.CharField(max_length = 60)

