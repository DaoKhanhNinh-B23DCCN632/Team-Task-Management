#type:ignore
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import ProjectForm, TaskForm

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
    form = ProjectForm() 
    if request.method == 'POST': 
        form = ProjectForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            messages.success(request, "New project was created successfully!")
            # return redirect('project')
    context = {'form': form}
    return render(request, 'main/create_project.html', context=context) 

def create_task(request):
    form = TaskForm()
    if request.method == 'POST': 
        form = TaskForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            messages.success(request, "Task was created successfully!") 
    context = {'form': form}
    return render(request, 'main/create_task.html', context=context)
def project(request): 
    return render(request, 'main/project.html')
def task(request): 
    return render(request, 'main/task.html')
def update_per_info(request): 
    return render(request, 'main/update_per_info.html')


