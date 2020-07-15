from django.shortcuts import render
from django.http import HttpResponse
from postjob.forms import PostingForm, SearchForm
from postjob.models import Jobform, Jobtype, Searchaddress
from datetime import timedelta, date, datetime
# Create your views here.

def posting(request):
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

def jobsearch(request):
    results = Jobform.objects.all()
    jobtypes = Jobtype.objects.all()
    search = request.GET.get('jobtitle')
    searchtype = request.GET.get('jobtype')
    searchaddress = request.GET.get('address')
    auth_req = request.GET.get('work_auth')
    minimum = request.GET.get('min_sal')
    duration = request.GET.get('posted_dur')
    today = date.today()
    form = SearchForm()

    if auth_req == "on":
        results = results.filter(US_author_required = True)

    if search != '' and search is not None:
        results = results.filter(title__icontains=search)

    if searchtype != '' and searchtype != 'Job Type':
        results = results.filter(jobtype__name=searchtype)

    if searchaddress != '' and searchaddress is not None:
        results = results.filter(address__icontains=searchaddress)

    if minimum != '' and minimum is not None:
        results = results.filter(salary_max__gte = minimum)

    if duration != '' and duration is not None:
        
        listjobs = [r.id for r in results if date.today() - r.postdate <= 5]
        results = results.filter(id__in=listjobs)

        
    return render(request, 'jobsearch.html', {'results': results, 'jobtypes':jobtypes, 'PostingForm':form})


def job_detail(request, job_id):
    try:
        job = Jobform.objects.get(id=job_id)
    except Job.DoesNotExist:
        raise Http404('Job not found')
    return render(request, 'job_detail.html', {'job': job,})