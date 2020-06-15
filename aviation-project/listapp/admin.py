from django.contrib import admin

# Register your models here.
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['jobID', 'title', 'jobtype', 'posted', 'deadline', 'now', 'valid_dates', 'open']
