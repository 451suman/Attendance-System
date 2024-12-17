from django.urls import path
from admin_app import views

app_name = 'a_app'

urlpatterns = [
    path('admin-login/', views.AdminLoginView.as_view(), name='admin-login'),
    path('admin-home/', views.AdminHomeView.as_view(), name='admin-home'),
]
