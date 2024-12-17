from django.urls import path

from attendance_app import views
from .views import AdminLoginView

urlpatterns = [path("admin_dashboard/", AdminLoginView.as_view(), name="admin_app")]
