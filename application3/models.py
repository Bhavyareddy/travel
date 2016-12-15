from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Facebook(models.Model):
	First_name =models.CharField(max_length= 20)
	Last_name =models.CharField(max_length= 20)
	Password =models.CharField(max_length= 20)
	Re_password =models.CharField(max_length= 20)
	Phone_no =models.IntegerField()
	Email_id =models.EmailField()
