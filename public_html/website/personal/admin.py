from django.contrib import admin

# Register your models here.

from personal.models import Project, Blog, Profile, ProjectImgs, AboutMe, Education, WorkExperience, Book

class ProfileAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

class BlogAdmin(admin.ModelAdmin):
    pass

class ProjectImgsAdmin(admin.ModelAdmin):
    pass

class AboutMeAdmin(admin.ModelAdmin):
    pass

class EducationAdmin(admin.ModelAdmin):
    pass

class WorkExperienceAdmin(admin.ModelAdmin):
    pass

class BookAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)

admin.site.register(Blog, BlogAdmin)

admin.site.register(Profile, ProfileAdmin)

admin.site.register(ProjectImgs, ProjectImgsAdmin)

admin.site.register(AboutMe, AboutMeAdmin)

admin.site.register(Education, EducationAdmin)

admin.site.register(WorkExperience, WorkExperienceAdmin)

admin.site.register(Book, BookAdmin)