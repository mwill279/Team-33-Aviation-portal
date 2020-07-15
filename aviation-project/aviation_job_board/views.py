from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from postjob.models import Jobtype
from postjob.forms import PostingForm, SearchForm

# Create your views here.
def home_view(request, *args, **kwargs):
    jobtypes = Jobtype.objects.all()
    form = SearchForm()
    return render(request, "index.html", {'jobtypes':jobtypes, 'PostingForm':form})

def companypage_view(request, *args, **kwargs):
    return render(request, "CompanyPage.html", {})

def postjob_view(request, *args, **kwargs):
    if request.method == 'POST':
        filled_form = PostingForm(request.POST)
        error = ''
        if filled_form.is_valid():
            if filled_form.cleaned_data['postdate'] > filled_form.cleaned_data['deadlinedate']:
                error = error + 'Error the date posted has to be before the deadline \n'
            if filled_form.cleaned_data['salary_min'] > filled_form.cleaned_data['salary_max']:
                error = error + 'Error the minimum salary has to be less than or equal to the maximum \n'
            if error == '':
                filled_form.save()
                note = '%s Posting has been submitted!!' %(filled_form.cleaned_data['title'],)
                new_form = PostingForm()
                return render(request, 'post_job.html', {'postingform':new_form, 'note':note})
            else:
                form = PostingForm()
                return render(request, 'post_job.html', {'postingform':filled_form, 'error':error})
    else: 
        form = PostingForm()
        return render(request, 'post_job.html', {'postingform':form,})

def chooseRegister_view(request, *args, **kwargs):
    return render(request, "choose_register.html", {})
