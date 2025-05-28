from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404
from taggit.models import Tag

from .models import Projects, Category
from .serializers import ProjectsSerializer, CategorySerializer, TagSerializer


class ProjectsAPIList(generics.ListAPIView):
    """Список всех проектов"""
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class ProjectsAPIRetrieve(generics.RetrieveAPIView):
    """Информация о конкретном проекте"""
    serializer_class = ProjectsSerializer

    def get_object(self):
        return get_object_or_404(Projects.objects, slug=self.kwargs['project_slug'])


class CategoryAPIList(generics.ListAPIView):
    """Список всех категорий"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjectsWithCategoriesAPIList(generics.ListAPIView):
    """Список проектов соответствующей категории"""
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        return Projects.objects.filter(cat__slug=self.kwargs['cat_slug'])


class TagAPIList(generics.ListAPIView):
    """Список всех тегов"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class ProjectsWithTagsAPIList(generics.ListAPIView):
    """Список проектов с соответствующим тегом"""
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        tag = get_object_or_404(Tag, slug=self.kwargs['tag_slug'])
        return Projects.objects.filter(tags__in=[tag])