from django.urls import path
from personal import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('blogs/', views.blogs, name='blogs'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('projects/<int:project_id>/', views.project_items, name='project_items'),
]