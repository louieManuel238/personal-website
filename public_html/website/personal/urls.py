from django.conf.urls import url
from personal import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^projects/', views.projects, name='projects'),
    url(r'^blogs/', views.blogs, name='blogs'),
    url(r'^aboutme/', views.aboutme, name='aboutme'),
]