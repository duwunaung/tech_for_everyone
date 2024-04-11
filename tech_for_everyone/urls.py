from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "T4E Admin"
admin.site.site_title = "T4E Admin Portal"
admin.site.index_title = "Welcome to T4E Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
