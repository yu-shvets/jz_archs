from django.views.generic import TemplateView, ListView, DetailView
from .models import Project, About, WorkExperienceWorkList, ProjectsWorkList, WorkshopsWorkList


class IndexView(ListView):
    model = Project
    template_name = 'index.html'
    queryset = Project.objects.all()


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'info.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        images = self.object.image_set.all().order_by('position')
        try:
            context['title_image'] = images[0]
        except IndexError:
            pass
        try:
            context['second_image'] = images[1]
        except IndexError:
            pass
        context['images'] = images[2:]
        return context


class AboutView(TemplateView):
    template_name = 'worklist.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['work_experience'] = WorkExperienceWorkList.objects.all()
        context['projects'] = ProjectsWorkList.objects.all()
        context['workshops'] = WorkshopsWorkList.objects.all()
        return context


class ContactView(AboutView):
    template_name = 'contact.html'



