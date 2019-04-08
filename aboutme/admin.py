from django.contrib import admin
from .models import PersonalInfo, Project, ProjectPicture


admin.site.register(PersonalInfo)


class ProjectPictureInline(admin.TabularInline):
    model = ProjectPicture
    fields = ['picture', ]


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectPictureInline, ]


admin.site.register(Project, ProjectAdmin)
