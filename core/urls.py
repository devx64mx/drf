
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.conf.urls.static import static  # type: ignore
from django.conf import settings # type: ignore

urlpatterns = [
    path('api/blog/', include('apps.blog.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )


