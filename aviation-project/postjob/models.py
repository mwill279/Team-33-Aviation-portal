from django.db import models
from django.core.validators import MinLengthValidator
from datetime import date, time, datetime
from datetime import timedelta
from datetime import timezone
from django.contrib.auth.models import User
# Create your models here.
class Jobtype(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Jobform(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    jobtype = models.ForeignKey(Jobtype, on_delete=models.CASCADE)
    #jobtype = models.ManyToManyField(Jobtype)
    description = models.TextField()
    datenow = datetime.date(datetime.now())
    timenow = datetime.time(datetime.now())
    # post = models.DateTimeField()
    # deadline = models.DateTimeField()
    postdate = models.DateField()
    posttime = models.TimeField()
    deadlinedate = models.DateField()
    deadlinetime = models.TimeField()
    zipcode = models.CharField(max_length=5, validators=[MinLengthValidator(5)], default='00000')
    def open(self):
        if self.postdate == self.datenow:
            return self.posttime <= self.timenow
        if self.deadlinedate == self.datenow:
            return self.deadlinetime >= self.timenow
        return (self.deadlinedate > self.datenow and self.postdate < self.datenow)

    # def valid_dates(self):
    #     return self.posted < self.deadline
