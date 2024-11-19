# rms/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Include allauth URLs
    path('', include('data_collection.urls', namespace='data_collection')),  # Include data_collection URLs with a namespace
    path('projects/', include('projects.urls')),
    path('participants/', include('participants.urls')),
    path('reports/', include('reports.urls')),
    path('users/', include('users.urls')),
]
