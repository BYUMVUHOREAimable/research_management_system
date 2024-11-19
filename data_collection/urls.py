# data_collection/urls.py

from django.urls import path
from . import views

app_name = 'data_collection'

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('add_researcher/', views.add_researcher, name='add_researcher'),
    path('edit_researcher/<int:pk>/', views.edit_researcher, name='edit_researcher'),
    path('delete_researcher/<int:pk>/', views.delete_researcher, name='delete_researcher'),
    path('add_project/', views.add_project, name='add_project'),
    path('edit_project/<int:pk>/', views.edit_project, name='edit_project'),
    path('delete_project/<int:pk>/', views.delete_project, name='delete_project'),
    path('projects/', views.project_list, name='project_list'),
    path('signup/', views.signup, name='signup'),  # Add the signup URL here
    path('login/', views.user_login, name='login'),  # Add the login URL here
]
