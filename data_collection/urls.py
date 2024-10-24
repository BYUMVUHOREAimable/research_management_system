from django.urls import path
from .views import (
    landing_page,
    add_researcher,
    edit_researcher,
    delete_researcher,
    add_project,
    edit_project,
    delete_project,
    project_list
)

from django.contrib import admin
from django.conf.urls import handler404
from data_collection.views import custom_404_view

handler404 = custom_404_view

app_name = 'data_collection'  # This is important for namespacing

urlpatterns = [
    path('', landing_page, name='landing_page'),  # Landing page
    path('add_researcher/', add_researcher, name='add_researcher'),
    path('edit_researcher/<int:pk>/', edit_researcher, name='edit_researcher'),
    path('delete_researcher/<int:pk>/', delete_researcher, name='delete_researcher'),
    path('add_project/', add_project, name='add_project'),
    path('edit_project/<int:pk>/', edit_project, name='edit_project'),
    path('delete_project/<int:pk>/', delete_project, name='delete_project'),
    path('projects/', project_list, name='project_list'),  # Project list page
]
