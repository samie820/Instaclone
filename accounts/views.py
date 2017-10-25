
from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserCreateForm
from feeds import urls
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def signup(request):
    form = UserCreateForm()

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.POST['username'])
            profile = UserProfile(user=user)
            profile.save()

            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request,new_user)
            
            return redirect('index')
    return render(request,'feeds/signup.html',{'form':form})


def login_user(request):
    
    form = AuthenticationForm()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
    
    return render(request,'feeds/login.html',{'form':form})

def signout(request):
    logout(request)
    return redirect('index')


def signup_success(request):
    return render(request, 'feeds/signup_success.html')