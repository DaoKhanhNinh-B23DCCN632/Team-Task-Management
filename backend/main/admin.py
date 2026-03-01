from django.contrib import admin
from .models import Users, Project, Task, TaskStatusHistory, ProjectMember, Notification
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin): 
    model = Users 
    fieldsets = UserAdmin.fieldsets + (
        (
            'Additional Info', {
                'fields': ('full_name', 'role'),
            }
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            'Additional Info', {
                'fields': ('full_name', 'role'),
            }
        ),
    )

admin.site.register(Users, CustomUserAdmin) 
admin.site.register(Task) 
admin.site.register(Project) 
admin.site.register(TaskStatusHistory) 
admin.site.register(ProjectMember) 
admin.site.register(Notification)



