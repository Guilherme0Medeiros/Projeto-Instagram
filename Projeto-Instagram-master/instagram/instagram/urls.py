# instagram/urls.py (URLs do projeto)
from django.contrib import admin  # Adicionando a importação do admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Inclui o painel de administração
    path('', include('instagram_app.urls')),  # Inclui as URLs do seu app
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

