from django.views.generic import TemplateView, ListView, DetailView
from .models import Project, About


class IndexView(ListView):
    model = Project
    template_name = 'index.html'
    queryset = Project.objects.all()


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'info.html'


class AboutView(TemplateView):
    template_name = 'worklist.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['about'] = About.objects.first()
        return context


class ContactView(AboutView):
    template_name = 'contact.html'



