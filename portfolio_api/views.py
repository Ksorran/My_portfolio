import os
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404
from taggit.models import Tag
from django.conf import settings
from rest_framework import status

from portfolio.models import Projects, Category, Feedback
from .serializers import ProjectsSerializer, CategorySerializer, TagSerializer, FeedbackSerializer


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


class ResumeAPI(APIView):
    """Endpoint для работы с файлом резюме. Поддерживает выдачу файла, его создание, замену и удаление."""
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.request.method != 'GET':
            return [permissions.IsAdminUser()]
        return super().get_permissions()

    @staticmethod
    def get_file_path():
        file_name = 'Resume_Glushko.pdf'
        return os.path.join(settings.MEDIA_ROOT, 'DRF', file_name)

    def get(self, request, *args, **kwargs):
        file_path = self.get_file_path()

        if not os.path.exists(file_path):
            return Response({'error': "Резюме не найдено!"}, status=status.HTTP_404_NOT_FOUND)

        return FileResponse(
            open(file_path, 'rb'),
            as_attachment=True,
            content_type='application/pdf'
        )

    def post(self, request, *args, **kwargs):
        file_path = self.get_file_path()

        if os.path.exists(file_path):
            return Response({'error': "Резюме уже существует, для изменения используйте метод PUT!"},
                            status=status.HTTP_400_BAD_REQUEST)

        if 'file' not in request.FILES:
            return Response({'error': "Файл не представлен!"}, status=status.HTTP_400_BAD_REQUEST)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb+') as destination:
            for chunk in request.FILES['file'].chunks():
                destination.write(chunk)

        return Response({'message': 'Резюме успешно загружено!'}, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        file_path = self.get_file_path()

        if not os.path.exists(file_path):
            return Response({'error': "Старая версия резюме не найдена!"}, status=status.HTTP_404_NOT_FOUND)

        if 'file' not in request.FILES:
            return Response({'error': "Файл не представлен!"}, status=status.HTTP_400_BAD_REQUEST)

        if os.path.exists(file_path):
            os.remove(file_path)

        with open(file_path, 'wb+') as destination:
            for chunk in request.FILES['file'].chunks():
                destination.write(chunk)

        return Response({'message': 'Резюме успешно обновлено!'}, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        file_path = self.get_file_path()

        if not os.path.exists(file_path):
            return Response({'error': "Резюме не найдено!"}, status=status.HTTP_404_NOT_FOUND)

        os.remove(file_path)
        return Response({'message': 'Резюме удалено!'}, status=status.HTTP_204_NO_CONTENT)


class FeedbackAPI(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]




