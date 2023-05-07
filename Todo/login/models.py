from datetime import date
from django import forms
from django.db import models

# Create your models here.

class Login(models.Model):
    Username = models.CharField(max_length=30)
    Password =  models.CharField(max_length=15)

    def __str__(self):
        return self.Username
    
class Register(models.Model):
    Username = models.CharField(max_length=30)
    Password = models.CharField(max_length=25)
    Email = models.EmailField()
    def __str__(self):
        return self.Username

class TodoList(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.title},{self.description}"

class TodoItem(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    duedate = models.DateField(default=date.today())
    is_complete = models.BooleanField(default=False)
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.todolist},{self.title},{self.description}"
    