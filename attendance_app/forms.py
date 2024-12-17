from django import forms

from attendance_app.models import Attendance

class AttendanceForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    class Meta:
        model = Attendance
        fields = [ "direction", "remarks" ]

