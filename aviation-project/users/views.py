from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, CompanyRegisterForm, CompanyUpdateForm
from django.core.files.storage import FileSystemStorage
from pyresparser import ResumeParser
from django.conf import settings
import os
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import Users
from .models import workExperience
from .models import educationExperience
from django.shortcuts import get_object_or_404
import datetime
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group


# Create your views here.
@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            #user = Users(Username = username, Email = email)

            group = Group.objects.get(name='jobseeker')
            user.groups.add(group)

            user.save()
            messages.success(request, f'Account Successfully Created! You May Now Log In')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@unauthenticated_user
def company_register(request):
    if request.method == 'POST':
        form = CompanyRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            group = Group.objects.get(name='company_owner')
            user.groups.add(group)

            user.save()
            messages.success(request, f'Account Successfully Created! You May Now Log In')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/company_register.html', {'form': form})

@login_required()
@allowed_users(allowed_roles=['company_owner'])
def company_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        username = u_form.cleaned_data.get('username')
        email = u_form.cleaned_data.get('email')
        user = Users(Username = username, Email = email)
        user.save()

        if u_form.is_valid():
            
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }

    return render(request, 'users/company_profile.html', context)
@login_required()
def resume(request):
    parsed_info = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['resume']
        if uploaded_file.name.endswith(".pdf") or uploaded_file.name.endswith(".docx"):
            fs = FileSystemStorage(location = os.path.join(settings.MEDIA_ROOT, 'resumes'))
            fs.save(uploaded_file.name, uploaded_file)
            path = os.path.join(settings.MEDIA_ROOT, 'resumes') + '/'+ uploaded_file.name
            parsed_info = ResumeParser(path).get_extracted_data()
            print(parsed_info)
            os.remove(path)
        else:
            print("Invalid Request")
    return render(request, 'users/resume.html', parsed_info)

@login_required()
@login_required()
@allowed_users(allowed_roles=['jobseeker'])
def jobseeker_profile_view(request):
	users = Users.objects.filter(Username = request.user.username)
	print(request.user.username)
	print(request.user.email)
	if not users.exists():
		print(request.user.username)
		print('111')
		user = Users(Username = request.user.username, Email = request.user.email)
		user.save()
	users = Users.objects.filter(Username = request.user.username)
	works = workExperience.objects.filter(Username = request.user.username)
	educations = educationExperience.objects.filter(Username = request.user.username)
	if request.method == 'POST' and 'editProfile' in request.POST:
		fullname = request.POST['name']
		nickname = request.POST['nickname']
		email = request.POST['email']
		phone = request.POST['phone']
		address = request.POST['address']
		thisuser = Users.objects.filter(Username = request.user.username).update(name = fullname, nickName = nickname, Email = email, phoneNumber = phone, Address = address)
		thatuser = User.objects.get(username = request.user.username, password = request.user.password)
		thatuser.email = email
		thatuser.save()
	if request.method == 'POST' and 'deleteWork' in request.POST:
		obj= works.get(comment = request.POST['comments'], job = request.POST['job'], company = request.POST['company'], Username = request.user.username).delete()
	if request.method == 'POST' and 'deleteEducation' in request.POST:
		obj= educations.get(duration = request.POST['duration'], title = request.POST['title'], school = request.POST['school'], Username = request.user.username).delete()
	return render (request, 'userProfile/profile2.html', {'users': users, 'works': works, 'educations': educations})








######################################################################################################################################################################################
######################################################################################################################################################################################
######################################################################################################################################################################################
######################################################################################################################################################################################
######################################################################################################################################################################################
######################################################################################################################################################################################
######################################################################################################################################################################################
######################################################################################################################################################################################
######################################################################################################################################################################################

def changepassword(request):
    if request.method == 'POST':
        oldpassword = request.POST['oldpass']
        newpass1 = request.POST['newpass1']
        newpass2 = request.POST['newpass2']

        if request.user.is_authenticated:
            thisuser = User.objects.get(username = request.user.username, password = request.user.password)
            #print(thisuser.username + "   " + thisuser.password)
            if thisuser is not None:
                print('user exists')
                if newpass1 == newpass2:
                    if len(newpass2) >= 6:
                        if any(c.isalpha() for c in newpass2):
                            #print('password matches')
                            #thisuser.set_password(newpass2)
                            thisuser.set_password(newpass2)
                            thisuser.save()
                            return redirect('/signin')
                        else:
                            messages.info(request, 'password must contain letter')
                            return redirect('/changepassword')
                    else:
                        messages.info(request, 'password too short')
                        return redirect('/changepassword')
                else:
                    messages.info(request, 'confirm password not match')
                    return redirect('/changepassword')
            else:
                messages.info(request, 'password incorrect')
                return redirect('/changepassword')
    else:
        return render(request, 'userProfile/changepassword.html')



def addWorkingExperience(request): 
    if request.method == 'POST':
        job = request.POST['job']
        years = request.POST['years']
        company = request.POST['company']
        comment = request.POST['comment']
        if request.user.is_authenticated:
            name = request.user.username
            works = workExperience(job = job, years = years, company = company, comment = comment, Username = name)
            works.save()
            return redirect('/userprofile')
    else:
        return render (request, 'userProfile/addwork.html')

def addEducationExperience(request): 
    if request.method == 'POST':
        title = request.POST['title']
        duration = request.POST['duration']
        school = request.POST['school']
        major = request.POST['major']
        if request.user.is_authenticated:
            name = request.user.username
            education = educationExperience(title = title, duration = duration, school = school, major = major, Username = name)
            education.save()
            return redirect('/userprofile')
    else:
        return render (request, 'userProfile/addeducation.html')



def about(request):
    return render (request, 'userProfile/profile2.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        nickname = request.POST['nickname']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        if User.objects.filter(username = username).exists():
            print('username taken')
            messages.info(request, 'username taken')
            return redirect('/signup')
        else:
            if len(password) >= 6:
                if any(c.isalpha() for c in password):
                    authuser = User.objects.create_user(username = username, password = password, email = email)
                    authuser.save()
                    user = Users(Username = username, name = name, nickName = nickname, Email = email, phoneNumber = phone, Address = address)
                    user.save()
                    return redirect('/signin')
                else:
                    messages.info(request, 'password must contain letter')
                    return redirect('/signup')
            else:
                messages.info(request, 'password too short')
                return redirect('/signup')
    else:
        return render (request, 'userProfile/signup.html')

# @unauthenticated_user
def signin(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']
        authuser = auth.authenticate(username = un, password = pw)

        if authuser is not None:
            auth.login(request, authuser)
            return redirect('/userprofile')

        else:
            messages.info(request, 'password or username invalid')
            return redirect('/signin')
    else:
        return render (request, 'userProfile/signin.html')

def upload(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        avatar = request.FILES.get('avatar')

        with open(avatar.name,'wb') as f:
            for line in avatar:
                f.write(line)
        return HttpResponse('ok')

    return render(request,'userProfile/upload.html')






    '''
        complete your profile before accessing.
    '''