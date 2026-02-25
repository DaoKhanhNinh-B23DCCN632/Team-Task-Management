from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('change_password/', views.change_password, name='change_password'), 
    path('create_project/', views.create_project, name='create_project'), 
    path('create_task/', views.create_task, name='create_task'), 
    path('project/', views.project, name='project'), 
    path('task/', views.task, name='task'), 
    path('update_per_info/', views.update_per_info, name='update_per_info') 
]