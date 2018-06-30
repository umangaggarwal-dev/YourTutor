from __future__ import unicode_literals
from django.db import models

class Progress(models.Model):
    #Everything we need to model the learning progress
    pass

class Student(models.Model):
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    email = models.EmailField()
    school = models.CharField(max_length = 100)

class Teacher(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()

class Course(models.Model):
    pass

class Topic(models.Model):
    pass

