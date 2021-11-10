from django.shortcuts import render
from django.urls import reverse_lazy
from projects.models import Project
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView


def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


class ProjectCreateView(CreateView):
    template_name = 'projects/create_project.html'
    model = Project
    success_url = reverse_lazy('create-new-project')
