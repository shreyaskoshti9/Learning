from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['name', 'email', 'addr1', 'addr2', 'empId', 'company_name', 'position', 'status', 'experience', 'salary', 'photo']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # class Meta:
    #     model = User
    #     fields = ['username',  'password']