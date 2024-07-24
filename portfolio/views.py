from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import Projects


class IndexView(TemplateView):
    template_name = 'portfolio/index.html'


class ProjectsHome(ListView):
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'
    extra_context = {'cat_selected': 0}

    def get_queryset(self):
        return Projects.objects.all()


class ProjectCategory(ListView):
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['projects'][0].cat
        context['cat_selected'] = cat.id
        return context

    def get_queryset(self):
        return Projects.objects.filter(cat__slug=self.kwargs['cat_slug'])


class ShowProject(DetailView):
    model = Projects
    template_name = 'portfolio/project.html'
    slug_url_kwarg = 'project_slug'
    context_object_name = 'project'

    def get_object(self, queryset=None):
        return get_object_or_404(Projects.objects, slug=self.kwargs[self.slug_url_kwarg])
