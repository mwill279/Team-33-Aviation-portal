from django.db import models
#from PIL import Image

# Create your models here.
class Profile(models.Model):
    #image = models.ImageField(default='default.png', upload_to='profile_pics')
    First_Name = models.CharField('First Name', max_length=100, default='', null=True, blank=True)
    Middle_Name = models.CharField('Middle Name', max_length=100, default='', null=True, blank=True)
    Last_Name = models.CharField('Last Name', max_length=100, default='', null=True, blank=True)

