from __future__ import unicode_literals
from django.db import models
import uuid
from datetime import datetime
from django.utils import timezone
 
GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'))

# Create your models here.
class Bus(models.Model):
	

	passenger_id = models.UUIDField(primary_key=True,  default=uuid.uuid4,  editable=False)
	passenger_name = models.CharField(max_length=50)
	mail_id = models.EmailField()
	age = models.IntegerField()
	arrival = models.CharField(max_length=30)
	destination = models.CharField(max_length=30)
	phone_number = models.IntegerField()
	date_of_jounery= models.DateField(auto_now_add=True,blank= True,null= True)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
