from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
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


# Create your views here.

def applicationStatus_view(request, *args, **kwargs):
    return render(request, "userprofile/applicationStatus.html", {})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            user = Users(Username = username, Email = email)
            user.save()
            messages.success(request, f'Account Successfully Created! You May Now Log In')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required()
def profile(request):
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

    return render(request, 'users/profile.html', context)


@login_required()
def resume(request):
    parsed_info = {}
    if request.method == 'POST' and 'upload' in request.POST:
        uploaded_file = request.FILES['resume']
        if uploaded_file.name.endswith(".pdf") or uploaded_file.name.endswith(".docx"):
            fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'resumes'))
            new_name = str(request.user.id) + uploaded_file.name
            fs.save(new_name, uploaded_file)
            path = os.path.join(settings.MEDIA_ROOT, 'resumes') + '/' + new_name
            parsed_info = ResumeParser(path).get_extracted_data()
            request.session['parsed_name'] = parsed_info.pop('name')
            request.session['parsed_email'] = parsed_info.pop('email')
            request.session['parsed_number'] = parsed_info.pop('mobile_number')
            request.session['parsed_skills'] = parsed_info.pop('skills')
            os.remove(path)
            return redirect('review')
        else:
            print("Invalid Request")
    return render(request, 'users/resume.html', parsed_info)


def review(request):
    if request.method == 'GET':
        return render(request, 'users/review.html',context={'name': request.session.get('parsed_name'),
                                                             'email': request.session.get('parsed_email'),
                                                             'mobile_number': request.session.get('parsed_number'),
                                                             'parsed_skills': request.session.get('parsed_skills')})
    if request.method == 'POST' and 'save' in request.POST:

        return redirect('userProfile-home')
    elif request.method == 'POST' and 'delete' in request.POST:
        skills = request.session.get('parsed_skills')
        print(skills)
        remove_skill = request.POST.get('delete')
        skills.remove(remove_skill)
        request.session['parsed_skills'] = skills
        return redirect('review')
    return render(request, 'users/review.html',  context={'name': request.session.get('parsed_name'),
                                                             'email': request.session.get('parsed_email'),
                                                             'mobile_number': request.session.get('parsed_number'),
                                                             'parsed_skills': request.session.get('parsed_skills')})


@login_required()
def home(request):
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
			findwork = workExperience.objects.filter(job = job, years = years, company = company, comment = comment, Username = name)
			if not findwork.exists():
				works = workExperience(job = job, years = years, company = company, comment = comment, Username = name)
				works.save()
			else:
				messages.info(request, 'Already have a same record.')
				return redirect('/addwork')
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
			findEducation = educationExperience.objects.filter(title = title, duration = duration, school = school, major = major, Username = name)
			if not findEducation.exists():
				education = educationExperience(title = title, duration = duration, school = school, major = major, Username = name)
				education.save()
			else: 
				messages.info(request, 'Already have a same record.')
				return redirect('/addeducation')
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