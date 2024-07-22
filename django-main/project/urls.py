
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from .views import home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('users/', include('users.urls')),
    path('bien_immobiliers/', include('bien_immobiliers.urls')),
    path('cart/', include('cart.urls')),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
