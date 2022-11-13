from django.conf.urls.static import static
from django.urls import include, path
from django.conf import settings
from django.contrib import admin

import Core.views


def custom_page_not_found(request):
    return Core.views.page_not_found_view(request, None)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("homepage.urls")),
    path("about/", include("about.urls")),
    path("catalog/", include("catalog.urls")),
    path('summernote/', include('django_summernote.urls')),
    path(r'404/', custom_page_not_found, )
]

handler404 = "Core.views.page_not_found_view"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += path('__debug__/', include('debug_toolbar.urls')),
