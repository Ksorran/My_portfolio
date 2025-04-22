from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from taggit.models import Tag

from .forms import FeedbackForm
from .models import Projects
from .utils import get_my_stack


class IndexView(TemplateView):
    """Главная страница сайта"""
    template_name = 'portfolio/index.html'
    extra_context = {'title': "Портфолио"}


class ResumeView(ListView):
    """Резюме"""
    template_name = 'portfolio/resume.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Projects.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["skills"] = get_my_stack()
        context["tags"] = [tag.slug for tag in Tag.objects.all()]
        context['title'] = 'Резюме'
        return context


class ProjectsHome(ListView):
    """Каталог проектов"""
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'
    extra_context = {'cat_selected': 0, 'title': 'Каталог'}

    def get_queryset(self):
        return Projects.objects.all()


class ProjectCategory(ListView):
    """Каталог проектов с учетом категорий"""
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


class ProjectTag(ListView):
    """Каталог проектов с учетом Тегов"""
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог'
        return context

    def get_queryset(self):
        tag = get_object_or_404(Tag, slug=self.kwargs['tag_slug'])
        return Projects.objects.filter(tags__in=[tag])


class ShowProject(DetailView):
    """Страница конкретного проекта"""
    model = Projects
    template_name = 'portfolio/project.html'
    slug_url_kwarg = 'project_slug'
    context_object_name = 'project'
    extra_context = {'title': 'Проект'}

    def get_object(self, queryset=None):
        return get_object_or_404(Projects.objects, slug=self.kwargs[self.slug_url_kwarg])


class ContactView(CreateView):
    """Обратная связь"""
    form_class = FeedbackForm
    template_name = 'portfolio/contact.html'
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Обратная связь'}
