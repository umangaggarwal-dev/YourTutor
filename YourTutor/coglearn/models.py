from __future__ import unicode_literals
from django.db import models

class Progress(models.Model):
    #Everything we need to model the learning progress
    studentid = models.OneToOneField(
        Student,
        on_delete = models.CASCADE
    )
    #learningGraph 
    #topic
    #subtopic
    #scoreInCurrentTopic
    #overallScore



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
    description = models.TextField
    start = models.OneToOneField(Topic, on_delete=CASCADE)

class Topic(models.Model):
    title = models.CharField(max_length=100)
    nextTopic = models.OneToOneField(Topic)
    subtopic = models.OneToOneField(SubTopic)
    #content


class SubTopic(models.Model):
    title = models.CharField(max_length = 100)
    nextSubTopic = models.OneToOneField(SubTopic)
    #content