from django.db import models
from datetime import date

# Create your models here.
class Project(models.Model):
    """
    Projects information
    """
    #fields
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    thumbnail_url = models.TextField(null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project-detail',args=[str(self.id)])

class Blog(models.Model):
    """
    Blog Information
    """
    #fields
    title = models.CharField(max_length=100)
    content = models.TextField()
    publishDate = models.DateTimeField(auto_now_add=True)
    thumbnail_url = models.TextField(null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog-detail',args=[str(self.id)])
    
class ProjectImgs(models.Model):
    """
    images for a project
    """
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    img_url = models.TextField()
    
    def __str__(self):
        return self.img_url
    
    def get_absolute_url(self):
        return reverse('project_Images',args=[str(self.id)])
    
class AboutMe(models.Model):
    """
        
    """
    
    
class Education(models.Model):
    """
    Educations and Trainings model
    """

class Hobbies(models.Model):
    """
    Books, Games
    """