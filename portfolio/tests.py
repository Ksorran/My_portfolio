from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from taggit.models import Tag, TaggedItem

from portfolio.models import Category, Projects


class PortfolioTestCase(TestCase):
    fixtures = ['portfolio_category.json', 'portfolio_feedback.json', 'portfolio_projects.json',
                'taggit_tag.json', 'taggit_taggeditem.json']

    def setUp(self):
        """Вручную добавляем теги в проекты, в соответствии с данными указанными в модели TaggedItem"""
        for item in TaggedItem.objects.all():
            project = Projects.objects.get(pk=item.object_id)
            project.tags.add(item.tag)

    def test_index(self):
        """Проверка домашней страницы"""
        path = reverse('home')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'portfolio/index.html')
        self.assertEqual(response.context_data['title'], 'Портфолио')

    def test_projects(self):
        """Проверка каталога проектов"""
        path = reverse('projects')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'portfolio/projects.html')
        self.assertEqual(response.context_data['title'], 'Каталог')

    def test_contact(self):
        """Проверка формы обратной связи"""
        path = reverse('contact')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'portfolio/contact.html')
        self.assertEqual(response.context_data['title'], 'Обратная связь')

    def test_category(self):
        """Проверка каталога проектов с учетом фильтра по категории"""
        categories = Category.objects.all()
        for category in categories:
            path = reverse('category', kwargs={'cat_slug': category.slug})
            response = self.client.get(path)
            self.assertEqual(response.status_code, HTTPStatus.OK)
            self.assertQuerysetEqual(response.context_data['projects'], Projects.objects.filter(cat=category),
                                     ordered=False)

    def test_tag(self):
        """Проверка каталога проектов с учетом фильтра по тегу"""
        tags = Tag.objects.all()
        for tag in tags:
            projects = Projects.objects.filter(tags__in=[tag])
            path = reverse('tags', kwargs={'tag_slug': tag.slug})
            response = self.client.get(path)
            self.assertEqual(response.status_code, HTTPStatus.OK)
            self.assertQuerysetEqual(response.context_data['projects'], projects, ordered=False)

    def test_project(self):
        """Проверка страницы проекта"""
        projects = Projects.objects.all()
        for project in projects:
            path = reverse('project', kwargs={'project_slug': project.slug})
            response = self.client.get(path)
            self.assertEqual(response.status_code, HTTPStatus.OK)
            self.assertTemplateUsed(response, 'portfolio/project.html')
            self.assertEqual(project.description, response.context_data['project'].description)

    def tearDown(self):
        pass