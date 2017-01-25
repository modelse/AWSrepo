from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Registrations
import re, bcrypt
EMAIL_REGEX=re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name=re.compile(r'^[a-zA-Z]')

#rendering html page
def index(request):
    return render(request, 'login/index.html')


def goback(request):
    return redirect('/')

#Login validation
def logins(request):
    if request.method=="POST":
        log=Registrations.objects.Login(request)
        print log
        if not log ==[]:
            for error in log:
                messages.info(request, error)
            return redirect('/')
        else:
            request.session['id']=Registrations.objects.only('id').get(email=request.POST['email2']).id
            request.session['username']=Registrations.objects.only('first_name').get(id=request.session['id']).first_name
            return redirect('/loginsuccess')

#Registering person
def register(request):
    errors=Registrations.objects.RegistrationValidation(request)
    # print errors
    if not errors ==[]:
        for error in errors:
            messages.info(request, error)
        return redirect('/')
    else:
        newUser=Registrations.objects.Register(request)
        return redirect('/success')
    return redirect('/')

#Render html for Successful Registration
def success(request):
    return render(request, 'login/yes.html')

#Render html for Successful login
def loginsuccess(request):
    return render(request, 'login/yay.html')


#Clearing sessions just for ease of manipulation
def clear(request):
    if request.method=="POST":
        del request.session['username']
        del request.session['id']
        return redirect('/')
