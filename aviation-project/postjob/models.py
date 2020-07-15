from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date, time, datetime, timezone
from mapbox_location_field.models import LocationField, AddressAutoHiddenField
from django_google_maps import fields as map_fields

class Jobtype(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Searchaddress(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)

class Jobform(models.Model):
    # company_id = models.IntegerField()
    title = models.CharField(max_length=100)
    jobtype = models.ForeignKey(Jobtype, on_delete=models.CASCADE)
    description = models.TextField()

    datenow = datetime.date(datetime.now())
    timenow = datetime.time(datetime.now())

    postdate = models.DateField()
    posttime = models.TimeField()

    deadlinedate = models.DateField()
    deadlinetime = models.TimeField()
    
    # location = LocationField()
    # address = AddressAutoHiddenField()

    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)

    salary_min = models.IntegerField()
    salary_max = models.IntegerField()

    US_author_required = models.BooleanField(default = False)


    def open(self):
        if self.postdate == self.datenow:
            return self.posttime <= self.timenow
        if self.deadlinedate == self.datenow:
            return self.deadlinetime >= self.timenow
        return (self.deadlinedate > self.datenow and self.postdate < self.datenow)


            
        
