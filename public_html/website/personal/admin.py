from django.contrib import admin

# Register your models here.

from personal.models import Project, Blog, Profile

class ProjectAdmin(admin.ModelAdmin):
	pass

admin.site.register(Project, ProjectAdmin)

class BlogAdmin(admin.ModelAdmin):
	pass

admin.site.register(Blog, BlogAdmin)

class ProfileAdmin(admin.ModelAdmin):
        pass

admin.site.register(Profile, ProfileAdmin)