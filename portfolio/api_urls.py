from django.urls import path
from . import api_views


urlpatterns = [
    path('v1/projects/', api_views.ProjectsAPIList.as_view()),
    path('v1/projects/categories/', api_views.CategoryAPIList.as_view()),
    path('v1/projects/categories/<slug:cat_slug>/', api_views.ProjectsWithCategoriesAPIList.as_view()),
    path('v1/projects/tags/', api_views.TagAPIList.as_view()),
    path('v1/projects/tags/<slug:tag_slug>/', api_views.ProjectsWithTagsAPIList.as_view()),
    path('v1/projects/<slug:project_slug>/', api_views.ProjectsAPIRetrieve.as_view()),
]