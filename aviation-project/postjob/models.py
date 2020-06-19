from django.db import models
from datetime import date, time
from datetime import timedelta
from datetime import timezone
# Create your models here.
class Jobtype(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Jobform(models.Model):
    title = models.CharField(max_length=100)
    jobtype = models.ForeignKey(Jobtype, on_delete=models.CASCADE)
    description = models.TextField()
    
    # post = models.DateTimeField()
    # deadline = models.DateTimeField()
    postdate = models.DateField()
    posttime = models.TimeField()
    deadlinedate = models.DateField()
    deadlinetime = models.TimeField()