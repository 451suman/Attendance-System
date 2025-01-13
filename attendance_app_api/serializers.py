from django.contrib.auth.models import Group, User
from rest_framework import serializers

from attendance_app.models import Attendance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "groups"]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name"]


class AttendanceSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Attendance
        fields = ["user", "direction", "remarks", "early_time", "late_time", "is_delete"]
        extra_kwargs ={
            "early_time":{"read_only":True},
            "late_time":{"read_only":True},
        }