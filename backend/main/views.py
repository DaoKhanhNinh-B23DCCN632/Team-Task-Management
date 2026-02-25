from django.shortcuts import render
from django.http import HttpResponse  


def login(request): 
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


