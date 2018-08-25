from django.contrib import admin

# Register your models here.

from personal.models import Project, Blog, Profile, ProjectImgs, AboutMe, Education, WorkExperience, Book

admin.site.register(Project)

admin.site.register(Blog)

admin.site.register(Profile)

admin.site.register(ProjectImgs)

admin.site.register(AboutMe)

admin.site.register(Education)

admin.site.register(WorkExperience)

admin.site.register(Book)