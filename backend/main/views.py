#type:ignore
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .forms import ProjectForm, TaskForm, ProfileForm, AddMemberForm
from .models import Users, Project
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.db.models import Q
def login(request): 
    if request.method == 'POST': 
        username = request.POST['username'] 
        password = request.POST['password'] 

        user = authenticate(request, username=username, password=password) 

        if user is not None: 
            auth_login(request, user) 
            return redirect('dashboard') 
        else: 
            messages.error(request, 'Username or Password incorrect!', extra_tags='login')
    return render(request, 'main/login.html')

@login_required

def dashboard(request): 
    return render(request, 'main/dashboard.html')

@login_required
def change_password(request, pk):
    user = Users.objects.get(id=pk)
    form = PasswordChangeForm(user)
    if request.user != user: 
        return redirect('update_per_info', pk=user.pk)
    if request.method == 'POST': 
        form = PasswordChangeForm(user, request.POST) 
        if form.is_valid(): 
            user = form.save() 
            update_session_auth_hash(request, user) 
            messages.success(request, "Change password completed!")
            return redirect('update_per_info', pk=user.pk) 
    form.fields['old_password'].widget.attrs.update({
        'class': 'border-2 border-gray-200 rounded-md w-[440px]', 
        'placeholder': 'Enter your current password'
    })
    form.fields['new_password1'].widget.attrs.update({
        'class': 'border-2 border-gray-200 rounded-md w-[440px]', 
        'placeholder': 'Enter your new password'
    })
    form.fields['new_password2'].widget.attrs.update({
        'class': 'border-2 border-gray-200 rounded-md w-[440px]', 
        'placeholder': 'Enter your new password again'
    })
    context = {'form': form, 'user': user} 
    return render(request, 'main/change_password.html', context=context) 

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

def create_task(request, pk):
    project = Project.objects.get(project_id = pk)
    form = TaskForm()
    if request.method == 'POST': 
        form = TaskForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            messages.success(request, "Task was created successfully!") 
    context = {'form': form, 'project':project}
    return render(request, 'main/create_task.html', context=context)
def project(request): 
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    projects = Project.objects.filter(
        Q(status_project__icontains=q) | 
        Q(project_name__icontains=q)
    ) 
    project_count = projects.count()
    statuses = Project.objects.values_list('status_project', flat=True).distinct()
    context = {'projects': projects, 'statuses': statuses, 'project_count': project_count}
    return render(request, 'main/project.html', context=context)

def task(request, pk):
    tasks = Project.objects.get(project_id = pk)
    project = Project.objects.get(project_id = pk)
    context = {'tasks': tasks, 'project': project} 
    return render(request, 'main/task.html', context=context)
def update_per_info(request, pk):  
    user = Users.objects.get(id=pk)
    form = ProfileForm(instance=user) 
    if request.method == 'POST': 
        form = ProfileForm(request.POST, instance=user) 
        if form.is_valid(): 
            form.save() 
            messages.success(request, "Personal information is updated!")
            return redirect('member') 
    context = {'form': form}
    return render(request, 'main/update_per_info.html', context=context)

def member(request): 
    users = Users.objects.all() 
    context = {'users': users}
    return render(request, 'main/member.html', context=context)


def delete_member(request, pk): 
    user = Users.objects.filter(id=pk).first() 

    if not user: 
        messages.warning(request, "User was deleted!")
        return redirect('member')
    if request.user.id == user.id: 
        return HttpResponseForbidden("You cannot delete yourself!")
    
    if request.method == 'POST':  
        user.delete() 
        messages.success(request, "User is deleted successfully!")
        redirect('member')
    context = {'user': user}
    return render(request, 'main/delete.html', context=context)

# def delete_project(request, pk): 



def add_member(request): 
    form = AddMemberForm() 
    if request.method == 'POST': 
        form = AddMemberForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            messages.success(request, 'User is added successfully!') 
            return redirect('member') 
    context = {'form': form} 
    return render(request, 'main/add_member.html', context=context)

def update_project(request, pk): 
    project = Project.objects.get(project_id=pk)
    user = Users.objects.get(id = project.created_by.id)
    form = ProjectForm(instance=project)
    if request.method == 'POST': 
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid(): 
            form.save() 
            messages.success(request, "Project is updated successfully!")
            return redirect('project')
    context = {'form': form, 'user': user, 'project': project}
    return render(request, 'main/update_project.html', context=context)