from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from postjob.models import Jobtype
from postjob.forms import PostingForm
from users.decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from users.models import User, Users
from postjob.models import Jobform

# Create your views here.

# from django import template
#
# register = template.Library()
# #
# @register.filter(name='has_group')
# def has_group(user, group_name):
#     return user.groups.filter(name=group_name).exists()


def base_view(request):
    # filter = True
    # allowed_roles = "jobseeker"
    # if request.user.groups.exists():
    #     group = request.user.groups.all()[0].name
    # if group in allowed_roles:
    #     filter = True

    #User.groups.filter()
    a_filter = True
    wtf = 'wtf'
    # if User.groups.get() == 'jobseeker':
    #     filter = True

    context = {
        'a_filter' : a_filter,
        'wtf' : wtf,
        # 'allowed_roles' : allowed_roles,
    }

    return render(request, "base.html", context=context)

def home_view(request):
    jobtypes = Jobtype.objects.all()

    context = {
        'jobtypes' : jobtypes,
    }

    return render(request, "index.html", context=context)

def portal_view(request, *args, **kwargs):
    return render(request, "profilePortal.html", {})

def companypage_view(request, *args, **kwargs):
    return render(request, "CompanyPage.html", {})

def chatRoom_view(request, *args, **kwargs):
    return render(request, "chat_room.html", {})

def searchpage_view(request, *args, **kwargs):
    return render(request, "search.html", {})

def postjob_view(request, *args, **kwargs):
    pj_form = PostingForm(request.POST)
    if request.method == 'POST':
        pj_form = PostingForm(request.POST)
        if pj_form.is_valid():
            title = pj_form.cleaned_data['title']
            description = pj_form.cleaned_data['description']
            #zipcode = pj_form.cleaned_data['zipcode']
            postdate = pj_form.cleaned_data['postdate']
            posttime = pj_form.cleaned_data['posttime']
            deadlinedate = pj_form.cleaned_data['deadlinedate']
            deadlinetime = pj_form.cleaned_data['deadlinetime']
            id = request.user.id
            Jobform.objects.filter(user_id=id).update(title=title, description=description, postdate=postdate, posttime=posttime, deadlinedate=deadlinedate, deadlinetime=deadlinetime)
            #message.success(request, f'Your job has been posted!')
            #pj_form.save()
            return redirect('company_profile')
        else:
            pj_form = PostingForm(request.POST)

    context = {
        'pj_form': pj_form,
    }
    return render(request, "post_job.html", context)

def chooseRegister_view(request, *args, **kwargs):
    return render(request, "choose_register.html", {})
