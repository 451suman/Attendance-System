
from django.urls import path

from attendance_app import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path("attendance/", views.AttendanceView.as_view(), name="attendance"),
    path("delete/<int:id>", views.DeleteAttendanceView.as_view(), name="delete")

]
