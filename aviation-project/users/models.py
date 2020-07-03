from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
# Create your models here.
# class User(AbstractUser):
#     is_user = models.BooleanField(default=False)
#     is_comanyEmployer = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'

class Users (models.Model): 
	Email = models.CharField(max_length = 40)
	Username = models.CharField(max_length = 20)
	name = models.CharField(max_length = 40, blank = True)
	Address = models.CharField(max_length = 40, blank = True)
	phoneNumber = models.CharField(max_length = 15, blank = True)
	nickName = models.CharField(max_length = 20, blank = True)
	password = models.CharField(max_length = 40, blank = True)
	image = models.ImageField(upload_to = 'profile_image', default = 'default.png')
	
	
class workExperience (models.Model):
	job = models.CharField(max_length = 40)
	years = models.CharField(max_length = 20)
	company = models.CharField(max_length = 30)
	comment = models.CharField(max_length = 150)
	Username = models.CharField(max_length = 20)

	
class educationExperience (models.Model):
	title = models.CharField(max_length = 40)
	duration = models.CharField(max_length = 20)
	school = models.CharField(max_length = 40)
	major = models.CharField(max_length = 40)
	Username = models.CharField(max_length = 20)
