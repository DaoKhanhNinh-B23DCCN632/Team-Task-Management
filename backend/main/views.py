#type:ignore
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .forms import ProjectForm, TaskForm, ProfileForm, AddMemberForm, AddCommentForm
from .models import Users, Project, Task, Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.db.models import Q
from django.utils import timezone
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
    user = Users.objects.all()
    projects = Project.objects.all()
    in_processing_projects = projects.filter(status_project='In processing').order_by('-start_date')[:4]
    in_processing_projects_count = in_processing_projects.count()
    completed_projects = projects.filter(status_project='Completed').order_by('-end_date')[:4] 
    completed_projects_count = completed_projects.count()
    upcoming_projects = projects.filter(status_project='Upcoming').order_by('start_date')[:4]
    upcoming_projects_count = upcoming_projects.count()
    total_projects = projects.count()
    date = timezone.now()
    context = {
        'users': user, 
        'in_processing_projects_count': in_processing_projects_count,
        'completed_projects_count': completed_projects_count,
        'upcoming_projects_count': upcoming_projects_count, 
        'total_projects': total_projects, 
        'date': date, 
        'in_processing_projects': in_processing_projects,
        'completed_projects': completed_projects,
        'upcoming_projects': upcoming_projects
    }
    return render(request, 'main/dashboard.html', context=context)

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
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    tasks = Task.objects.filter(
        (Q(status__icontains=q) | 
        Q(task_name__icontains=q))&
        Q(project_id = pk)
    )
    status_count = tasks.count()
    project = Project.objects.get(project_id = pk)
    statuses = [s[0] for s in Task.status_choices]
    context = {'tasks': tasks, 'project': project, 'statuses': statuses, 'status_count': status_count} 
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

def update_task(request, pk):
    task = Task.objects.get(task_id=pk)
    project = Project.objects.get(project_id=task.project_id.project_id)
    form = TaskForm(instance=task) 
    if request.method == 'POST': 
        form = TaskForm(request.POST, instance=task)
        if form.is_valid(): 
            form.save() 
            messages.success(request, "Task is updated successfully!") 
            return redirect('task', pk=task.project_id.project_id)
    context = {'form': form, 'task': task, 'project': project}
    return render(request, 'main/update_task.html', context=context)    

def delete_project(request, pk):
    project = Project.objects.filter(project_id=pk).first() 

    if not project: 
        messages.warning(request, "Project was deleted!")
        return redirect('project')
    
    if request.method == 'POST':  
        project.delete() 
        messages.success(request, "Project is deleted successfully!")
        return redirect('project')
    context = {'project': project}
    return render(request, 'main/delete_project.html', context=context)

def delete_task(request, pk):
    task = Task.objects.filter(task_id = pk).first() 

    if not task: 
        messages.warning(request, "Task was deleted!")
        return redirect('task', pk=task.project_id.project_id) 
    
    if request.method == 'POST': 
        task.delete() 
        messages.success(request, "Task is deleted successfully!")
        return redirect('task', pk=task.project_id.project_id)
    context = {'task': task}
    return render(request, 'main/delete_task.html', context=context)
def comment(request, pk): 
    project = Project.objects.get(project_id=pk) 
    comments = Comment.objects.filter(project_id=project)
    context = {'project': project, 'comments': comments} 
    return render(request, 'main/comment.html', context=context) 

def add_comment(request, pk):
    project = Project.objects.get(project_id=pk)
    form = AddCommentForm() 
    if request.method == 'POST': 
        form = AddCommentForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            messages.success(request, 'Comment is added successfully!') 
            return redirect('comment', pk=pk)

    context = {'form': form, 'project': project} 
    return render(request, 'main/add_comment.html', context=context)

def update_comment(request, pk): 
    comment = Comment.objects.get(comment_id=pk)
    project = Project.objects.get(project_id=comment.project_id.project_id)
    form = AddCommentForm(instance=comment)
    if request.method == 'POST': 
        form = AddCommentForm(request.POST, instance=comment)
        if form.is_valid(): 
            form.save() 
            return redirect('comment', pk=project.project_id) 
    context = {'form': form, 'project': project, 'comment': comment}
    return render(request, 'main/update_comment.html', context=context)
def delete_comment(request, pk):
    comment = Comment.objects.filter(comment_id=pk).first() 
    project = Project.objects.get(project_id=comment.project_id.project_id)
    if not comment: 
        messages.warning(request, "Comment was deleted!")
        return redirect('comment', pk=comment.project_id.project_id) 
    
    if request.method == 'POST': 
        comment.delete() 
        messages.success(request, "Comment is deleted successfully!")
        return redirect('comment', pk=comment.project_id.project_id)
    context = {'comment': comment, 'project': project}
    return render(request, 'main/delete_comment.html', context=context)