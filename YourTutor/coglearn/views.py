from __future__ import unicode_literals
from django.shortcuts import render

def index(request):
    return render (request, 'index.html')

def dashboard(request):
	return render(request,'dashboard.html')

def signup(request):
	return render(request,'signup.html')