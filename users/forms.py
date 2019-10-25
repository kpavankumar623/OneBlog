from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name']

class ProfileUpdateForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False)
    phone = forms.IntegerField(required=False)

    class Meta:
        model = UserProfile
        fields = ['phone','profile_picture']
