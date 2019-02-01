# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login as django_login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import user_form


# Create your views here.

def home(request):
    return render(request,'app/home.html')



def regester(request):
    if request.method=="POST":
        form = user_form(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            return HttpResponseRedirect(request,'app/home.html')
    else:
        form=user_form()
    return render(request , 'app/regesteration.html',{'form':form})


def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username , password=password)

        if user is not None:
            django_login(request, user)
            return render(request,'app/home.html',{'username':username})
        else:
            return HttpResponse("failed :( ")
    else:
        return render(request,'app/login.html')



@login_required
def logoff(request):
    logout(request)
    return render(request,'app/home.html')
