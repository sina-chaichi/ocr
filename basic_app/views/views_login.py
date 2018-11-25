from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm

#

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print('Someone tried to login and failed')
            print('Username: {} and Password: {}'.format(username,password))
            return HttpResponse('Invalid login details supplied!')
    else:
        return render(request,'basic_app/login.html',{})
