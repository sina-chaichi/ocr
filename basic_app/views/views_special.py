from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm

#

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required




@login_required
def special(request):
    return HttpResponse('You are logged in, Nice!')
