from django import forms
from .models import Student
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=['username','email','password']

class StudentForm(forms.ModelForm):
    class Meta():
        model=Student
        fields=['firstName','lastName','progress','school']