from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace="users")),
    path("__debug__/", include("debug_toolbar.urls")),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('api/', include('portfolio_api.urls')),
    path('', include('portfolio.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'Панель администрирования'
admin.site.index_title = 'Мое портфолио'