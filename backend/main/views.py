from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login(request): 
    if request.method == 'POST': 
        username = request.POST['username'] 
        password = request.POST['password'] 

        user = authenticate(request, username=username, password=password) 

        if user is not None: 
            auth_login(request, user) 
            return redirect('dashboard') 
        else: 
            messages.error(request, 'Username or Password incorrect!')
    return render(request, 'main/login.html')


def dashboard(request): 
    return render(request, 'main/dashboard.html')


def change_password(request): 
    return render(request, 'main/change_password.html') 
def create_project(request): 
    return render(request, 'main/create_project.html') 
def create_task(request): 
    return render(request, 'main/create_task.html')
def project(request): 
    return render(request, 'main/project.html')
def task(request): 
    return render(request, 'main/task.html')
def update_per_info(request): 
    return render(request, 'main/update_per_info.html')


