from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('change_password/', views.change_password, name='change_password'), 
    path('create_project/', views.create_project, name='create_project'), 
    path('create_task/', views.create_task, name='create_task'), 
    path('project/', views.project, name='project'), 
    path('task/', views.task, name='task'), 
    path('update_per_info/', views.update_per_info, name='update_per_info'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='main/password_reset.html'), name='password_reset'), 
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'), 
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'), 
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]