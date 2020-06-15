from datetime import datetime
from datetime import timedelta
from datetime import timezone
from django.db import models

# Create your models here.
class Job(models.Model):
    TYPE_CHOICES = [('F', 'Full Time'), ('P', 'Part Time'), ('I', 'Internship')]
    jobID = models.IntegerField(null=False, unique=True)
    title = models.CharField(max_length=100)
    jobtype = models.CharField(max_length=1, choices=TYPE_CHOICES, blank=True)
    description = models.TextField()
    posted = models.DateTimeField()
    deadline = models.DateTimeField()
    now = datetime.now(timezone.utc)
    
    def open(self): 
        return self.deadline > self.now and self.posted < self.now

    def valid_dates(self):
        return self.posted < self.deadline