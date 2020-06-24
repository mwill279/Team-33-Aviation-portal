from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostingForm
from postjob.models import Jobform, Jobtype
# Create your views here.

def posting(request):
    if request.method == 'POST':
        filled_form = PostingForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            note = '%s Posting submitted!!' %(filled_form.cleaned_data['title'],)
            new_form = PostingForm()
            return render(request, 'posting.html', {'postingform':new_form, 'note':note})
    else: 
        form = PostingForm()
        return render(request, 'posting.html', {'postingform':form})

def jobsearch(request):
    results = Jobform.objects.all()
    jobtypes = Jobtype.objects.all()
    search = request.GET.get('jobtitle')
    searchtype = request.GET.get('jobtype')



    if search != '' and search is not None:
        results = results.filter(title__icontains=search)

    if searchtype != '' and searchtype != 'Job Type':
        results = results.filter(jobtype__name=searchtype)
        
    return render(request, 'jobsearch.html', {'results': results, 'jobtypes':jobtypes,})

















def fulltime(request):
    results = Jobform.objects.filter(jobtype=1)
    return render(request, 'jobsearch.html', {'results': results,})

def parttime(request):
    results = Jobform.objects.filter(jobtype=2)
    return render(request, 'jobsearch.html', {'results': results,})

def internship(request):
    results = Jobform.objects.filter(jobtype=3)
    return render(request, 'jobsearch.html', {'results': results,})

def job_detail(request, job_id):
    try:
        job = Jobform.objects.get(id=job_id)
    except Job.DoesNotExist:
        raise Http404('Job not found')
    return render(request, 'job_detail.html', {'job': job,})