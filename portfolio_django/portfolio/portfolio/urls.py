from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    ## Home Page
    path("", include("home.urls", namespace="home")),
    ## Interface Admin
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler400 = "home.views.handle_bad_request"
handler403 = "home.views.handle_permission_denied"
handler404 = "home.views.handle_not_found"
handler500 = "home.views.handle_server_error"
