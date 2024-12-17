from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("attendance_app.urls")),
    path("", include("admindashboard.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]

# Add this for serving static files in development
# i f settings.DEBUG:
#     u rlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
