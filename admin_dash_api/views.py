from rest_framework import permissions
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from rest_framework import viewsets
from admin_dash_api.serializers import UserListserializer,UserAttendanceSerializer
from attendance_app.models import Attendance

class ListUserViewSet(ListAPIView):
    queryset = User.objects.all() 
    serializer_class = UserListserializer
    permission_classes = [permissions.IsAdminUser]
    