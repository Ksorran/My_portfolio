from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('projects/', views.ProjectsHome.as_view(), name='projects'),
    path('category/<slug:cat_slug>/', views.ProjectCategory.as_view(), name='category'),
    path('project/<slug:project_slug>/', views.ShowProject.as_view(), name='project'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]