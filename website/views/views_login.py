from django.shortcuts import render
from users.forms import UserForm,UserProfileInfoForm
from django.contrib.auth.models import User
#

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def get_user(email):
    try:
        return User.objects.get(email=email.lower())
    except User.DoesNotExist:
        return None

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = get_user(email)


        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print('Someone tried to login and failed')
            print('Email: {} and Password: {}'.format(email,password))
            return HttpResponse('Invalid login details supplied!')
    else:
        return render(request,'relatedpages/login.html',{})

@login_required
def special(request):
    return HttpResponse('You are Signeed in, Nice!')
