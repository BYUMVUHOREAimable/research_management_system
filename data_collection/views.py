from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Researcher, ResearchProject
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Landing Page
@login_required
def landing_page(request):
    researchers = Researcher.objects.all()
    projects = ResearchProject.objects.all()
    return render(request, 'data_collection/landing_page.html', {'researchers': researchers, 'projects': projects})

# Add Researcher
@login_required
def add_researcher(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name and email:
            Researcher.objects.create(name=name, email=email)
            messages.success(request, "Researcher added successfully.")
            return redirect('data_collection:landing_page')
        else:
            messages.error(request, "Both name and email are required.")
    return render(request, 'data_collection/add_researcher.html')

# Edit Researcher
@login_required
def edit_researcher(request, pk):
    researcher = get_object_or_404(Researcher, pk=pk)
    if request.method == 'POST':
        researcher.name = request.POST.get('name')
        researcher.email = request.POST.get('email')
        researcher.save()
        messages.success(request, "Researcher updated successfully.")
        return redirect('data_collection:landing_page')
    return render(request, 'data_collection/edit_researcher.html', {'researcher': researcher})

# Delete Researcher
@login_required
def delete_researcher(request, pk):
    researcher = get_object_or_404(Researcher, pk=pk)
    if request.method == 'POST':
        researcher.delete()
        messages.success(request, "Researcher deleted successfully.")
        return redirect('data_collection:landing_page')
    return render(request, 'data_collection/delete_researcher.html', {'researcher': researcher})

# Add Project
@login_required
def add_project(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        researcher_id = request.POST.get('researcher')
        if title and researcher_id:
            try:
                researcher = Researcher.objects.get(pk=researcher_id)
                project = ResearchProject.objects.create(title=title, researcher=researcher, created_at=timezone.now())
                messages.success(request, "Project added successfully.")
                return redirect('data_collection:project_list')
            except Researcher.DoesNotExist:
                messages.error(request, "Selected researcher does not exist.")
        else:
            messages.error(request, "Both project title and researcher are required.")
    researchers = Researcher.objects.all()
    return render(request, 'data_collection/add_project.html', {'researchers': researchers})

# Edit Project
@login_required
def edit_project(request, pk):
    project = get_object_or_404(ResearchProject, pk=pk)
    if request.method == 'POST':
        project.title = request.POST.get('title')
        researcher_id = request.POST.get('researcher')
        if researcher_id:
            try:
                researcher = Researcher.objects.get(pk=researcher_id)
                project.researcher = researcher
                project.save()
                messages.success(request, "Project updated successfully.")
                return redirect('data_collection:landing_page')
            except Researcher.DoesNotExist:
                messages.error(request, "Selected researcher does not exist.")
        project.save()
        messages.success(request, "Project updated successfully.")
        return redirect('data_collection:landing_page')
    return render(request, 'data_collection/edit_project.html', {'project': project})

# Delete Project
@login_required
def delete_project(request, pk):
    project = get_object_or_404(ResearchProject, pk=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Project deleted successfully.")
        return redirect('data_collection:landing_page')
    return render(request, 'data_collection/delete_project.html', {'project': project})

# Project List
@login_required
def project_list(request):
    projects = ResearchProject.objects.all().select_related('researcher')
    return render(request, 'data_collection/project_list.html', {'projects': projects})

# Custom 404 page
def custom_404_view(request, exception):
    return render(request, 'data_collection/404.html', status=404)

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after signup
            messages.success(request, "Signup successful! Redirecting to the landing page.")
            return redirect('data_collection:landing_page')  # Redirect to landing page after signup
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})

# Login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful! Redirecting to the landing page.")
            return redirect('data_collection:landing_page')  # Redirect to landing page after login
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'account/login.html')
