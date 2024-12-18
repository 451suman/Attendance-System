from django.urls import path
from admindashboard import views

app_name = 'a_app'

urlpatterns = [
    path('admin-dashboard-login/', views.AdminLoginView.as_view(), name='admin-dashboard-login'),
    path('admin-dashboard-logout/', views.AdminLogoutView.as_view(), name='admin-dashboard-logout'),
    path('admin-dashboard-home/', views.AdminHomeView.as_view(), name='admin-dashboard-home'),
    path("admin-dashboard-attendances/<int:pk>", views.AttendanceListuser.as_view(), name='admin-dashboard-attendances'),
]
