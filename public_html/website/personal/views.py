from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'personal/index.html')

def projects(request):
    return render(request, 'personal/projects.html')