from django.shortcuts import render, redirect, get_object_or_404
from .models import Researcher, ResearchProject  # Ensure your models are correctly imported
from django.http import HttpResponse
from django.utils import timezone

# Landing Page
def landing_page(request):
    researchers = Researcher.objects.all()
    projects = ResearchProject.objects.all()
    return render(request, 'data_collection/landing_page.html', {'researchers': researchers, 'projects': projects})

# Add Researcher
def add_researcher(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        if name and email:  # Check if both fields are filled
            Researcher.objects.create(name=name, email=email)
            return redirect('data_collection:landing_page')  # Redirect to landing page
        else:
            return HttpResponse("Both name and email are required.", status=400)

    return render(request, 'data_collection/add_researcher.html')


# Edit Researcher
def edit_researcher(request, pk):
    researcher = get_object_or_404(Researcher, pk=pk)
    if request.method == 'POST':
        researcher.name = request.POST.get('name')
        researcher.email = request.POST.get('email')
        researcher.save()
        return redirect('data_collection:landing_page')  # Use namespaced URL
    return render(request, 'data_collection/edit_researcher.html', {'researcher': researcher})

# Delete Researcher
def delete_researcher(request, pk):
    researcher = get_object_or_404(Researcher, pk=pk)
    if request.method == 'POST':
        researcher.delete()
        return redirect('data_collection:landing_page')  # Use namespaced URL
    return render(request, 'data_collection/delete_researcher.html', {'researcher': researcher})

# Add Project
def add_project(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        researcher_id = request.POST.get('researcher')  # Ensure this matches your select name
        
        if title and researcher_id:
            try:
                researcher = Researcher.objects.get(pk=researcher_id)
                project = ResearchProject.objects.create(title=title, researcher=researcher, created_at=timezone.now())
                return redirect('data_collection:project_list')  # Use namespaced URL
            except Researcher.DoesNotExist:
                return HttpResponse("Selected researcher does not exist.", status=400)
        else:
            return HttpResponse("Both project title and researcher are required.", status=400)

    researchers = Researcher.objects.all()
    return render(request, 'data_collection/add_project.html', {'researchers': researchers})

# Edit Project
def edit_project(request, pk):
    project = get_object_or_404(ResearchProject, pk=pk)
    
    if request.method == 'POST':
        project.title = request.POST.get('title')
        researcher_id = request.POST.get('researcher')  # Allow changing the researcher
        
        if researcher_id:  # Check if a researcher is provided
            try:
                researcher = Researcher.objects.get(pk=researcher_id)
                project.researcher = researcher  # Update researcher
            except Researcher.DoesNotExist:
                return HttpResponse("Selected researcher does not exist.", status=400)

        project.save()
        return redirect('data_collection:landing_page')  # Use namespaced URL
    return render(request, 'data_collection/edit_project.html', {'project': project})

# Delete Project
def delete_project(request, pk):
    project = get_object_or_404(ResearchProject, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('data_collection:landing_page')  # Ensure the correct namespaced URL
    return render(request, 'data_collection/delete_project.html', {'project': project})


# Project List
def project_list(request):
    projects = ResearchProject.objects.all().select_related('researcher')  # Optimize by selecting related researchers
    return render(request, 'data_collection/project_list.html', {'projects': projects})

#404 page
def custom_404_view(request, exception):
    return render(request, 'data_collection/404.html', status=404)
