from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth import authenticate

from attendance_app.models import Attendance
from .serializers import AttendanceSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
# class UserAttendanceViewSet(viewsets.ModelViewSet):

#     queryset = Attendance.objects.all()
#     serializer_class = AttendanceSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         queryset = queryset.filter(user=self.request.user)
#         return queryset



class UserAttendanceViewSet(APIView):
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None, pk=None):
        
        attendance = Attendance.objects.filter(user=self.request.user)
        serializer= AttendanceSerializer(attendance, many=True)
        return Response(serializer.data)
        
