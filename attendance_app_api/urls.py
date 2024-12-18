from django.urls import include, path
from rest_framework import routers
from attendance_app_api import views

router = routers.DefaultRouter()
router.register(r'user-attendance', views.UserAttendanceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
 path('', include(router.urls)),    
]