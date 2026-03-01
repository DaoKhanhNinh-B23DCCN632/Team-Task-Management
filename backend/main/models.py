from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.

class Users(AbstractUser): 
    full_name = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return self.username 

class Project(models.Model): 
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100, blank=True, null=True) 
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True) 
    end_date = models.DateTimeField(blank=True, null=True) 
    created_by = models.ForeignKey(
        Users, 
        on_delete=models.PROTECT, 
        related_name='projects'
    )

    def __str__(self):
        return self.project_name

class Task(models.Model): 
    task_id = models.AutoField(primary_key=True) 
    task_name = models.CharField(max_length=100, blank=True, null=True) 
    description = models.TextField(blank=True, null=True) 
    status = models.CharField(max_length=50, blank=True, null=True) 
    deadline = models.DateTimeField(blank=True, null=True)
    project_id = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE, 
        related_name='tasks' 
    )

    def __str__(self):
        return self.task_name

class TaskStatusHistory(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE) 
    task_id = models.ForeignKey(
        Task, 
        on_delete=models.CASCADE, 
        related_name='status_history'
    )
    old_status = models.CharField(max_length=20, blank=True, null=True)
    new_status = models.CharField(max_length=20, blank=True, null=True)
    changed_at = models.DateTimeField(blank=True, null=True) 

class ProjectMember(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE) 
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    role_in_project = models.CharField(max_length=50)
    joined_at = models.DateTimeField(blank=True, null=True)

class Notification(models.Model): 
    notification_id = models.AutoField(primary_key=True) 
    message = models.TextField(blank=True, null=True) 
    user_id = models.ForeignKey(
        Users, 
        on_delete=models.CASCADE, 
        related_name='notifications'
    )
    









