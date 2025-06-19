from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user, get_user_model

from taggit.managers import TaggableManager


class Projects(models.Model):
    """База данных, содержащая информацию о моих Pet-проектах"""

    class Status(models.IntegerChoices):
        PLANNED = 0, 'В планах'
        AT_WORK = 1, 'В работе'
        FINISH = 2, 'Закончен'

    title = models.CharField(max_length=255, verbose_name="Название проекта")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title_screen = models.ImageField(upload_to='screenshots/', default='def_im/default_pr.png',
                                     null=True, blank=True, verbose_name='Лицевой скриншот')
    description = models.TextField(blank=True, verbose_name="Описание проекта")
    code_description = models.TextField(blank=True, verbose_name="Описание кода")
    additional_information = models.TextField(blank=True, verbose_name="Дополнительная информация")
    technology_stack = models.TextField(blank=True, verbose_name="Стек технологий")
    code_screen = models.ImageField(upload_to='screenshots/', default='def_im/default_pr.png', null=True, blank=True,
                                    verbose_name='Скрин кода')
    interface_screen = models.ImageField(upload_to='screenshots/', default='def_im/default_pr.png', null=True, blank=True,
                                         verbose_name='Скрин интерфейса')
    github_link = models.URLField(null=True, blank=True, verbose_name='Ссылка на гитхаб')
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    project_stage = models.IntegerField(choices=Status.choices, default=Status.PLANNED, verbose_name='Статус')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория', null=True, blank=True,
                            related_name='projects')
    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проекты'
        verbose_name_plural = 'Проекты'

    def get_absolute_url(self):
        return reverse('project', kwargs={'project_slug': self.slug})


class Category(models.Model):
    """Категории, на которые подразделяются Pet-проекты"""
    name = models.CharField(max_length=255, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class Feedback(models.Model):
    """Содержит все сообщения из обратной связи. Полагаю рассматриваемый функционал не соответствует логике данного
    приложения и его следует перенести, но создавать исключительно под него отдельное приложение считаю избыточным,
    поэтому изменения будут по мере расширения проекта"""
    user = models.ForeignKey(get_user_model(), verbose_name="автор", on_delete=models.SET_NULL, null=True)
    contacts = models.CharField(verbose_name='Удобный для Вас способ связи', max_length=255, blank=True)
    feedback = models.TextField(verbose_name="Сообщение")

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'
