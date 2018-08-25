from django.db import models

# Create your models here.
class Profile(models.Model):
    """
    Basic information about the user
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    title = models.CharField(max_length=225, null=True)
    photo = models.TextField(null=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('profile',args=[str(self.id)])
    
class Project(models.Model):
    """
    Projects information
    """
    #fields
    title = models.CharField(max_length=225)
    description = models.TextField()
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
    publishDate = models.DateTimeField(auto_now=True, blank=True)
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
        Personal Information
    """
    personalDescription = models.TextField(null=True)
    personalImg = models.CharField(max_length=300, null=True)
    hobbyDescription = models.TextField(null=True)
    hobbyImg = models.CharField(max_length=300, null=True)
    
    def __str__(self):
        return self.personalDescription
    
    def get_absolute_url(self):
        return reverse('about_me',args=[str(self.id)])
    
class Education(models.Model):
    """
    Educations and Trainings model
    """
    title = models.CharField(max_length=225,null=True)
    startDate = models.IntegerField(null=True)
    endDate = models.IntegerField(null=True)
    institution = models.CharField(max_length=225,null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('education',args=[str(self.id)])
    
class WorkExperience(models.Model):
    """
    Work Experiences
    """
    title = models.CharField(max_length=225,null=True)
    startDate = models.IntegerField(null=True)
    endDate = models.IntegerField(null=True)
    institution = models.CharField(max_length=225,null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('work_experience',args=[str(self.id)])
