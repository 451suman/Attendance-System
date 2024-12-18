from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("jwt_authentication_api.urls")),
    path("api/", include("attendance_app_api.urls")),

    path("", include("attendance_app.urls")),
    path("", include("admindashboard.urls")),
]
