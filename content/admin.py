from django.contrib import admin
from .models import Project, Image, About, WorkExperienceWorkList, ProjectsWorkList, WorkshopsWorkList


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)
    exclude = ('slug',)
    list_display = ('name', 'position')


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


admin.site.register(About, AboutAdmin)
admin.site.register(WorkExperienceWorkList)
admin.site.register(ProjectsWorkList)
admin.site.register(WorkshopsWorkList)
