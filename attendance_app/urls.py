
from django.urls import path

from attendance_app import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path("user-login/", views.UserLoginView.as_view(), name="user-login"),
    path("user-logout/", views.UserLogoutView.as_view(), name="user-logout"),
    path("attendance/", views.AttendanceView.as_view(), name="attendance"),
    path("delete/<int:id>", views.DeleteAttendanceView.as_view(), name="delete")

]
