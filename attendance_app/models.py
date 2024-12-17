from django.db import models
from django.contrib.auth.models import User
# Create your models here.

Direction_Choice =(
    ('Check In','Check In'),
    ('Check Out','Check Out'),
    ('Personal Out',"Personal Out"),
    ('Personal In',"Personal In"),
)
class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    direction = models.CharField(max_length=100, choices=Direction_Choice, null=False, blank=False)
    remarks = models.TextField(max_length=200, null=False, blank=False)
    time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)
    late_by = models.TimeField(null=True, blank=True)
    early_by = models.TimeField(null=True, blank=True)


    def __str__(self):
        return self.user.username