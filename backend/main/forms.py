from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, Select
from .models import Project 

class ProjectForm(ModelForm): 
    class Meta:
        model = Project 
        fields = '__all__'  
        widgets = {
            'project_name': TextInput(attrs={
                'class': 'border-2 border-gray-200 rounded-md w-[400px]'
            }), 
            'description': Textarea(attrs={
                'placeholder': 'Describe project in detail...', 
                'class': 'border-2 border-gray-200  w-[400px] h-48 rounded-md'
            }), 
            'start_date': DateTimeInput(attrs={
                "class": "border-2 border-gray-200 rounded-md w-60"
            }),
            'end_date': DateTimeInput(attrs={
                "class": "border-2 border-gray-200 rounded-md w-60"
            }),
            'created_by': Select(attrs={
                'class': 'border-2 border-gray-200 rounded-md'
            })
        }
    