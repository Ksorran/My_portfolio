from django.contrib import admin
from .models import Projects, Category, Feedback


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'project_stage', 'cat')
    list_display_links = ('id', 'title')
    ordering = ('id',)
    list_editable = ('project_stage', 'cat', )
    list_per_page = 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name')
    ordering = ('id', )


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'contacts', 'feedback')
    list_display_links = ('id', 'user')
    ordering = ('id', )
