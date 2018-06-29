from __future__ import unicode_literals
from django.shortcuts import render
# for login and logout
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm

def index(request):
    return render (request, 'index.html')

def dashboard(request):
	return render(request,'dashboard.html')


def signup(request):

    registered=False
    if request.method =='POST':
        user_form=UserForm(request.POST or None)
        profile_form=Student(request.POST or None,request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user_form.cleaned_data.get('password'))
            username=user_form.cleaned_data.get('username')
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
           # Update our variable to tell the template registration was successful.
            registered=True
            login(request,user)
    else:
        user_form=UserForm()
        profile_form=StudentForm()

    return render(request,'signup.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
