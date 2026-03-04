# type: ignore
from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('change_password/<str:pk>/', views.change_password, name='change_password'), 
    path('create_project/', views.create_project, name='create_project'), 
    path('create_task/', views.create_task, name='create_task'), 
    path('project/', views.project, name='project'), 
    path('task/<str:pk>', views.task, name='task'), 
    path('member/', views.member, name='member'),
    path('update_per_info/<str:pk>/', views.update_per_info, name='update_per_info'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='main/password_reset.html'), name='password_reset'), 
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password_reset_done.html'), name='password_reset_done'), 
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='main/password_reset_confirm.html'), name='password_reset_confirm'), 
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password_reset_complete.html'), name='password_reset_complete'),
    path('delete_member/<str:pk>', views.delete_member, name='delete_member'), 
    path('add_member/', views.add_member, name='add_member'), 
    path('update_project/<str:pk>', views.update_project, name='update_project')
]