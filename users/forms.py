from django import forms
from django.contrib.auth.models import User
from users.models import UserProfileInfo
from orders.models import Document

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')



class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)
