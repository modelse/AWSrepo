from __future__ import unicode_literals
import re, bcrypt
from django.db import models
EMAIL_REGEX=re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name=re.compile(r'^[a-zA-Z]')

class UserManager(models.Manager):
    def RegistrationValidation(self, request):
        errors=[]
        if len(request.POST['first_name'])<2:
            errors.append('First name needs more characters.')
        elif not name.match(request.POST['first_name']):
            errors.append('No numbers allowed in first name')
        if len(request.POST['last_name'])<2:
            errors.append('Last name needs more characters.')
        elif not name.match(request.POST['last_name']):
            errors.append('No numbers allowed in last name.')
        if not EMAIL_REGEX.match(request.POST['email']):
            errors.append('Not a valid email address.')
        if len(request.POST['password'])<9:
            errors.append('Password needs to be 9 characters or more!')
        if request.POST['password']!=request.POST['confirm']:
            errors.append('Password does not match!')
        return errors
    def Register(self, request):
        password=(request.POST['password'])
        hashed= bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        Registrations.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed)

    def Login(self,request):
        errors=[]
        print request.POST['password2']
        if len(Registrations.objects.filter(email=request.POST['email2']))==1:
            Registrations.objects.get(email=request.POST['email2'])
            incPassword=request.POST['password2']
            storedPassword=Registrations.objects.only('password').get(email=request.POST['email2']).password
            if bcrypt.hashpw(incPassword.encode(), storedPassword.encode())  == storedPassword:
                print "it works"
                
            else:
                errors.append("Email and password do not match!")
            return errors
        else:
            errors.append("Email does not exist")
        return errors


class Registrations(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects=UserManager()
# Create your models here.
