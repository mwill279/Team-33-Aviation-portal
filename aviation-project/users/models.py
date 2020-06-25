from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
# class User(AbstractUser):
#     is_user = models.BooleanField(default=False)
#     is_comanyEmployer = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
