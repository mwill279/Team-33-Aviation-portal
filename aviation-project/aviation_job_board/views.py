from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from postjob.models import Jobtype
from postjob.forms import PostingForm

# Create your views here.
def home_view(request, *args, **kwargs):
    jobtypes = Jobtype.objects.all()
    return render(request, "index.html", {'jobtypes':jobtypes})

def companypage_view(request, *args, **kwargs):
    return render(request, "CompanyPage.html", {})

def postjob_view(request, *args, **kwargs):
    if request.method == 'POST':
        filled_form = PostingForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = '%s Posting submitted!!' %(filled_form.cleaned_data['title'],)
            new_form = PostingForm()
            return render(request, 'post_job.html', {'postingform':new_form, 'note':note})
    else: 
        form = PostingForm()
        return render(request, 'post_job.html', {'postingform':form})
    return render(request, "post_job.html", {})

def chooseRegister_view(request, *args, **kwargs):
    return render(request, "choose_register.html", {})
