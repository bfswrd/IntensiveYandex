from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("homepage.urls")),
    path("about/", include("about.urls")),
    path("catalog/", include("catalog.urls")),
    path('summernote/', include('django_summernote.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
