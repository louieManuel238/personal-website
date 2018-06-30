from django.shortcuts import render
from . models import Blog, Project

# Create your views here.
def index(request):
    blog_list = Blog.objects.all()[:3]
    project_list = Project.objects.all()[:2]
    return render(request, 'personal/index.html', {'blogs': blog_list, 'projects': project_list})

def projects(request):
    return render(request, 'personal/projects.html')

def blogs(request):
    blog_list = Blog.objects.all()
    return render(request, 'personal/blogs.html', context={'list': blog_list})

def aboutme(request):
    return render(request, '')


		