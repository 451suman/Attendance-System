from django.contrib import admin

from attendance_app.models import Attendance

# Register your models here.
# admin.site.register(Attendance)
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display =[ "user", "direction", "remarks", "time", "is_delete"]
    list_filter = ["is_delete","time","direction"]
    search_fields = ('user__username', 'direction')
