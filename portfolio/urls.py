from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('resume/', views.ResumeView.as_view(), name='resume'),
    path('projects/', views.ProjectsHome.as_view(), name='projects'),
    path('category/<slug:cat_slug>/', views.ProjectCategory.as_view(), name='category'),
    path('project/<slug:project_slug>/', views.ShowProject.as_view(), name='project'),
    path('tag/<slug:tag_slug>/', views.ProjectTag.as_view(), name='tags'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]