from rest_framework import serializers
from django.contrib.auth.models import User

from attendance_app.models import Attendance


class UserListserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id",'username',"email","first_name", "last_name","is_staff")
        read_only_fields = fields

class UserAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = [ "id", "user", "direction", "remarks", "time", "is_delete", "late_time", "early_time"]

        extra_kwargs ={
            "late_time":{"read_only":True},
            "early_time":{"read_only":True},
        }