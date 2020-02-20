from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .decorator import unautehticated_user,allowed_users,admin_only

@login_required(login_url='login')
@admin_only
def home(request):
    return render(request, 'accounts/home.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def user(request):
    return render(request,'accounts/user.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def admin(request):
    return render(request,'accounts/admin.html')

@unautehticated_user
def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html',{'error':'username has already been taken'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'accounts/signup.html',{'error':'password must match'})
    else:
        return render(request,'accounts/signup.html')

def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{"error":"username or password is incorrect!"})
    else:
        return render(request,'accounts/login.html')


def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')
