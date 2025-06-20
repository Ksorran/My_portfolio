from django.urls import path, include
from portfolio_api import views

urlpatterns = [
    path('v1/projects/', views.ProjectsAPIList.as_view()),
    path('v1/projects/categories/', views.CategoryAPIList.as_view()),
    path('v1/projects/categories/<slug:cat_slug>/', views.ProjectsWithCategoriesAPIList.as_view()),
    path('v1/projects/tags/', views.TagAPIList.as_view()),
    path('v1/projects/tags/<slug:tag_slug>/', views.ProjectsWithTagsAPIList.as_view()),
    path('v1/projects/<slug:project_slug>/', views.ProjectsAPIRetrieve.as_view()),
    path('v1/drf-auth/', include('rest_framework.urls')),
    path('v1/auth/', include('djoser.urls')),
    path('v1/resume/', views.ResumeAPI.as_view()),
    path('v1/feedback/', views.FeedbackAPI.as_view()),
]