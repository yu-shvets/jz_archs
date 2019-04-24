from django.contrib import admin
from .models import Project, Image, About


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


admin.site.register(About, AboutAdmin)

