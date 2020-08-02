from django.db import models

# Create your models here.
class Users (models.Model): 
	Email = models.CharField(max_length = 40)
	Username = models.CharField(max_length = 20)
	name = models.CharField(max_length = 40)
	address = models.CharField(max_length = 40)
	phoneNumber = models.CharField(max_length = 10)
	nickName = models.CharField(max_length = 20)
	password = models.CharField(max_length = 40)
	
	
class workExperience (models.Model):
	job = models.CharField(max_length = 40)
	years = models.CharField(max_length = 20)
	company = models.CharField(max_length = 30)
	comment = models.CharField(max_length = 150)
	Username = models.CharField(max_length = 20)

    