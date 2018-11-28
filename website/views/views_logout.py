from django.shortcuts import render
from users.forms import UserForm,UserProfileInfoForm

#

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
