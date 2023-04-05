from django.db import models
from django import forms

# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    testScore = models.FloatField()
    

class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Todo(models.Model):
    username = models.CharField( max_length=20)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)