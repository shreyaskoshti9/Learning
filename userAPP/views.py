from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.

User = get_user_model()

def home(request):
    return render(request, 'userAPP/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()

    
    return render(request, 'registration/register.html', {'form': form})       


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if user:
                login(request, user)
                return redirect('home')
            else:
                print("Login Failed")    
    else:
        form = LoginForm()
        
    return render(request, 'registration/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return render(request, 'base.html')

@login_required
def userDetails(request):
    if request.method == "POST":
        form = UserDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            details = form.save(commit=False)
            details.user = request.user
            details.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = UserDetailsForm()

    return render(request, 'userAPP/details.html', {'form': form})
            
