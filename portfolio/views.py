from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView

from .forms import FeedbackForm
from .models import Projects


class IndexView(TemplateView):
    template_name = 'portfolio/index.html'
    extra_context = {'title': "Портфолио"}


class ProjectsHome(ListView):
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'
    extra_context = {'cat_selected': 0, 'title': 'Каталог'}

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
        context['title'] = 'Каталог'
        return context

    def get_queryset(self):
        return Projects.objects.filter(cat__slug=self.kwargs['cat_slug'])


class ShowProject(DetailView):
    model = Projects
    template_name = 'portfolio/project.html'
    slug_url_kwarg = 'project_slug'
    context_object_name = 'project'
    extra_context = {'title': 'Проект'}

    def get_object(self, queryset=None):
        return get_object_or_404(Projects.objects, slug=self.kwargs[self.slug_url_kwarg])


class ContactView(LoginRequiredMixin, CreateView):
    form_class = FeedbackForm
    template_name = 'portfolio/contact.html'
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Обратная связь'}
