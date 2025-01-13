from datetime import time, datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import pytz  # Import pytz directly

Direction_Choice = (
    ("Check In", "Check In"),
    ("Check Out", "Check Out"),
)


class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    direction = models.CharField(
        max_length=100, choices=Direction_Choice, null=False, blank=False
    )
    remarks = models.TextField(max_length=200, null=False, blank=False)
    time = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    @property
    def late_time(self):
        """
        Calculate how late the user is if the attendance direction is 'Check In'.
        This is based on the Django project's configured time zone (e.g., Asia/Kathmandu).
        """
        if self.direction == "Check In" and self.time:
            # Convert the stored time to the project's time zone (Asia/Kathmandu)
            entry_time = self.time.astimezone(pytz.timezone("Asia/Kathmandu"))

            # Define office start time (9 AM local time in Kathmandu)
            check_in_time = time(9, 0, 0)

            # Create the check-in datetime for comparison
            check_in_datetime = entry_time.replace(
                hour=check_in_time.hour,
                minute=check_in_time.minute,
                second=0,
                microsecond=0,
            )

            # If the user checked in after 9 AM (entry time)
            if entry_time > check_in_datetime:
                time_diff = entry_time - check_in_datetime
                return (
                    datetime.min + time_diff
                ).time()  # Return the late time as a time object
            else:
                return None  # No late time if checked in before 9 AM
        return None  # Return None if direction is not 'Check In'

    @property
    def early_time(self):
        """
        Calculate how early the user is if the attendance direction is 'Check Out'.
        This is based on the Django project's configured time zone (e.g., Asia/Kathmandu).
        """
        if self.direction == "Check Out" and self.time:
            # Convert the stored time to the project's time zone (Asia/Kathmandu)
            entry_time = self.time.astimezone(pytz.timezone("Asia/Kathmandu"))

            # Define office close time (6 PM local time in Kathmandu)
            check_out_time = time(18, 0, 0)

            # Create the check-out datetime for comparison
            check_out_datetime = entry_time.replace(
                hour=check_out_time.hour,
                minute=check_out_time.minute,
                second=0,
                microsecond=0,
            )

            # If the user checked out before 6 PM (entry time)
            if entry_time < check_out_datetime:
                time_diff = check_out_datetime - entry_time
                return (
                    datetime.min + time_diff
                ).time()  # Return the early time as a time object
            else:
                return None  # No early time if checked out after 6 PM
        return None  # Return None if direction is not 'Check Out'
