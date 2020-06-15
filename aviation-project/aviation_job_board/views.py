from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})

def companypage_view(request, *args, **kwargs):
    return render(request, "CompanyPage.html", {})

def postjob_view(request, *args, **kwargs):
    return render(request, "post_job.html", {})