from django.shortcuts import render
from . models import Blog, Project, ProjectImgs

# Create your views here.
def index(request):
    blog_list = Blog.objects.all()[:3]
    project_list = Project.objects.all()[:2]
    return render(request, 'personal/index.html', {'blogs': blog_list, 'projects': project_list})

def projects(request):
    project_list = Project.objects.all()
    return render(request, 'personal/projects.html', {'projects': project_list})

def blogs(request):
    blog_list = Blog.objects.all()
    return render(request, 'personal/blogs.html', context={'list': blog_list})

def aboutme(request):
    return render(request, '')

def project_items(request, project_id="0"):
    project_imgs = ProjectImgs.objects.filter(project_id_id = project_id)
    project_item = Project.objects.get(id__exact=project_id)
    return render(request, 'personal/project_items.html', {'project': project_item, 'imgs':project_imgs})

		