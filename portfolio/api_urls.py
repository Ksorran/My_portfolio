from django.urls import path, include, re_path
from . import api_views


urlpatterns = [
    path('v1/projects/', api_views.ProjectsAPIList.as_view()),
    path('v1/projects/categories/', api_views.CategoryAPIList.as_view()),
    path('v1/projects/categories/<slug:cat_slug>/', api_views.ProjectsWithCategoriesAPIList.as_view()),
    path('v1/projects/tags/', api_views.TagAPIList.as_view()),
    path('v1/projects/tags/<slug:tag_slug>/', api_views.ProjectsWithTagsAPIList.as_view()),
    path('v1/projects/<slug:project_slug>/', api_views.ProjectsAPIRetrieve.as_view()),
    path('v1/drf-auth/', include('rest_framework.urls')),
    path('v1/auth/', include('djoser.urls')),
    path('v1/resume/', api_views.ResumeAPI.as_view()),
    path('v1/feedback/', api_views.FeedbackAPI.as_view()),
]