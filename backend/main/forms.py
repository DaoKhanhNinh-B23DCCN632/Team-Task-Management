#type: ignore
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, Select, EmailInput
from .models import Project, Task, Users, Comment

class ProjectForm(ModelForm): 
    class Meta:
        model = Project 
        fields = '__all__'  
        widgets = {
            'project_name': TextInput(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-[calc(100%-20px)]',
                'placeholder': 'Enter project name ...'
            }), 
            'description': Textarea(attrs={
                'placeholder': 'Describe project in detail...', 
                'class': 'border-2 border-gray-200  w-[calc(100%-20px)] h-48 rounded-md'
            }), 
            'start_date': DateTimeInput(attrs={
                "class": "border-2 border-gray-200 rounded-md w-[calc(100%-20px)]"
            }),
            'end_date': DateTimeInput(attrs={
                "class": "border-2 border-gray-200 rounded-md w-[calc(100%-20px)]"
            }),
            'created_by': Select(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-[calc(100%-20px)]'
            }), 
            'status_project': Select(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-[calc(100%-20px)]'
            })
        }

class TaskForm(ModelForm): 
    class Meta: 
        model = Task 
        fields = [
            'task_name', 
            'description', 
            'status', 
            'deadline', 
            'assign_to', 
            'project_id'
        ]
        widgets = {
            'task_name': TextInput(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-full'
            }), 
            'description': Textarea(attrs={
                'class': 'border-2 border-gray-200  w-full h-48 rounded-md'
            }), 
            'status': Select(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-[calc(100%-1000px)]'
            }), 
            'deadline': DateTimeInput(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-[calc(100%-1000px)]'
            })
        }

class ProfileForm(ModelForm): 
    class Meta: 
        model = Users 
        fields = [
            'full_name', 
            'gender', 
            'date_of_birth', 
            'role', 
            'email', 
            'username'
        ] 
        widgets = {
            'full_name': TextInput(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-80'
            }), 
            'gender': Select(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-80'
            }), 
            'date_of_birth': DateTimeInput(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-80'
            }), 
            'role': Select(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-80'
            }), 
            'email': EmailInput(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-80'
            }), 
            'username': TextInput(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-80'
            })
        }

class AddMemberForm(ModelForm): 
    class Meta: 
        model = Users 
        fields = [
            'full_name', 
            'gender', 
            'date_of_birth', 
            'role', 
            'email', 
            'username'
        ] 
        widgets = {
            'full_name': TextInput(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-80'
            }), 
            'gender': Select(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-80'
            }), 
            'date_of_birth': DateTimeInput(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-80'
            }), 
            'role': Select(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-80'
            }), 
            'email': EmailInput(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-80'
            }), 
            'username': TextInput(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-80'
            })
        }

class AddCommentForm(ModelForm): 
    class Meta: 
        model = Comment 
        fields = ['content', 'project_id', 'user_name'] 
        widgets = {
            'content': Textarea(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-full h-48'
            }), 
            'user_name': TextInput(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-full'
            }),
            'project_id': Select(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-full'
            })
        }

