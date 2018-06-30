from __future__ import unicode_literals
from django.shortcuts import render
# for login and logout
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import UserForm


def dashboard(request):
	return render(request,'dashboard.html')


def index(request):
    registered=False
    try:
        user=request.user
        username=UserProfile.objects.get(user=user)
        registered=True
    except:
        pass
    if request.method =='POST' and not registered:
        form=UserForm(request.POST or None)

        if form.is_valid():
            user=form.save()
            user.set_password(form.cleaned_data.get('password'))
            username=form.cleaned_data.get('username')
            user.save()
           # Update our variable to tell the template registration was successful.
            registered=True
            login(request,user)
    else:
        form=UserForm()
    return render(request,'index.html',{'form':form})