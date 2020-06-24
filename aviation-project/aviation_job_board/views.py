from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from postjob.models import Jobtype

# Create your views here.
def home_view(request, *args, **kwargs):
    jobtypes = Jobtype.objects.all()
    return render(request, "index.html", {'jobtypes':jobtypes})

def companypage_view(request, *args, **kwargs):
    return render(request, "CompanyPage.html", {})

def postjob_view(request, *args, **kwargs):
    return render(request, "post_job.html", {})