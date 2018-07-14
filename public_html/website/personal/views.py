from django.shortcuts import render
from . models import Blog, Project, ProjectImgs
import requests

# Create your views here.
def index(request):
    blog_list = Blog.objects.all()[:3]
    project_list = Project.objects.all()[:2]
    response = requests.get('http://localhost:8001/api/v1/bucketlist/1/')
    data = response.json()
    return render(request, 'personal/index.html', {'blogs': blog_list, 'projects': project_list, 'title': data['title']})

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

		