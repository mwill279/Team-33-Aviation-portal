from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile
from .models import Users
from .models import workExperience
from .models import educationExperience

# Register your models here.
admin.site.register(Profile)
admin.site.register(User)
admin.site.register(Users)
admin.site.register(workExperience)
admin.site.register(educationExperience)
