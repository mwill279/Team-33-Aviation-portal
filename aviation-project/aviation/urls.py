"""aviation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from listapp import views as listapp_views
from postjob import views as postjob_views

from aviation_job_board.views import home_view,portal_view, companypage_view, postjob_view
from users import views as user_views
from events_app.views import events_view
urlpatterns = [
    path('', home_view, name='home'),
    path('portal/', portal_view, name='portal_view'),
    path('company/',companypage_view, name='company_page'),
    path('admin/', admin.site.urls),
    path('jobpost/', postjob_view, name='post_job'),
    path('events/', events_view, name='event_list'),
    path('register/', user_views.JobSeekerSignUpView.as_view(), name='register'),
    path('resume/', user_views.JobSeekerSignUpView.as_view(), name='resume'),
   #path('profile/', user_views.userProfileView.as_view(template_name='users/profile.html'), name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('postjob/', postjob_views.posting, name='posting'),
    path('jobsearch/', postjob_views.jobsearch, name='jobsearch'),
    path('jobsearch/<int:job_id>/', postjob_views.job_detail, name='job_detail'),
#    path('fulltime/', postjob_views.fulltime, name='fulltime'),
#    path('parttime/', postjob_views.parttime, name='parttime'),
#    path('internship/', postjob_views.internship, name='internship'),
]

"""aviation URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from postjob import views as postjob_views

from aviation_job_board.views import home_view, companypage_view, postjob_view, chooseRegister_view
from users import views as user_views
from events_app.views import events_view
urlpatterns = [
    path('', home_view, name='home'),
    path('company/',companypage_view, name='company_page'),
    path('admin/', admin.site.urls),
    path('jobpost/', postjob_view, name='post_job'),
    path('events/', events_view, name='event_list'),
    path('user_register/', user_views.JobSeekerSignUpView.as_view(), name='register'),
    path('company_register/', user_views.CompanySignUpView.as_view(), name='company_register'),
    path('resume/', user_views.JobSeekerSignUpView.as_view(), name='resume'),
    path('user_profile/', user_views.JobSeekerSignUpView.as_view(), name='profile'),
    path('company_profile/', user_views.CompanySignUpView.as_view(), name='profile'),
    path('choose_register/', chooseRegister_view, name='choose_register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('postjob/', postjob_views.posting, name='posting'),
    path('jobsearch/', postjob_views.jobsearch, name='jobsearch'),
    path('jobsearch/<int:job_id>/', postjob_views.job_detail, name='job_detail'),
    path('userprofile/', user_views.home, name = 'userProfile-home'),
    path('about/', user_views.about, name = 'userProfile-about'),
    path('signup/', user_views.signup, name = 'userProfile-signup'),
    path('addwork/', user_views.addWorkingExperience, name = 'userProfile-addwork'),
    path('addeducation/', user_views.addEducationExperience, name = 'userProfile-addeducation'),
    path('signin/', user_views.signin, name = 'userProfile-signin'),
    path('changepassword/', user_views.changepassword, name = 'userProfile-changepassword'),
    path('upload/', user_views.upload, name = 'userProfile-upload')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)