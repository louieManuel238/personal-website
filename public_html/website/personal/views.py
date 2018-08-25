from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect

from .forms import ContactForm
from . models import Blog, Project, ProjectImgs, Profile, AboutMe, Education, WorkExperience, Book

# Create your views here.
def index(request):
    blog_list = Blog.objects.all()[:3]
    project_list = Project.objects.all()[:2]
    profile = Profile.objects.get(pk = 1)
    return render(request, 'personal/index.html', {'blogs': blog_list, 'projects': project_list, 'profile': profile})

def projects(request):
    project_list = Project.objects.all()
    return render(request, 'personal/projects.html', {'projects': project_list})

def blogs(request):
    blog_list = Blog.objects.all()
    return render(request, 'personal/blogs.html', context={'list': blog_list})

def aboutme(request):
    about_me = AboutMe.objects.get(pk = 1)
    education = Education.objects.order_by('-endDate','-startDate')
    workExperience = WorkExperience.objects.order_by('-endDate','-startDate')
    book = Book.objects.all()
    return render(request, 'personal/aboutme.html', context={'aboutMe': about_me,
'education':education, 'workExperience':workExperience, 'book':book})

def project_items(request, project_id="0"):
    project_imgs = ProjectImgs.objects.filter(project_id = project_id)
    project_item = Project.objects.get(id__exact=project_id)
    return render(request, 'personal/project_items.html', {'project': project_item, 'imgs':project_imgs})

def contact(request):
    form = ContactForm(request.POST)
    if(form.is_valid()):
        message = form.cleaned_data['message']
        email = form.cleaned_data['email']
        try:
            send_mail("From Personal Website: "+email, message, email, ['manuel.gayao@outlook.com'])
        except BadHeaderError:
            return HttpResponseRedirect(request.path_info)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))