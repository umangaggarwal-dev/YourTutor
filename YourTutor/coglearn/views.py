from __future__ import unicode_literals
from django.shortcuts import render
from .models import Topic

def login(request):
    return render (request, 'login.html')


def home(request):
    return render(request, 'home.html', context={"topics" : [topic for topic in Topic.objects.get(title = 'English').get_children()]})