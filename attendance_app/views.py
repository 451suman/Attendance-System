from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from attendance_app.forms import AttendanceForm, UserLoginForm
from attendance_app.models import Attendance
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.urls import reverse_lazy
from datetime import datetime, time, timedelta


class UserLoginView(FormView):
    template_name = "registration/login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(username =username, password= password)
        if user is not None:
            if user.is_superuser is False:
                messages.success(self.request, "Login successfull")
                login (self.request, user)
            else:
                messages.error(self.request, "you dont have permission to login")
        else:
            messages.error(self.request, "Login Unsuccessfull")

        return super().form_valid(form)

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("user-login")


class USERloginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser is False:
            pass
        else:
            return redirect('user-login')  

        return super().dispatch(request, *args, **kwargs)




class HomeView(USERloginRequiredMixin, TemplateView):
    template_name = "home.html"

    def get_context_data(self):
        context = super().get_context_data()

        context["attendances"] = Attendance.objects.filter(user=self.request.user, is_delete=False).order_by("-time")

        # context{"late_by": 27, "early_by": 0}
        return context


# Attendance view
class AttendanceView(View):
    template_name = "attendance/attendance.html"
    form_class = AttendanceForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        direction = request.POST.get('direction')

        user = authenticate(username=username, password=password)
        if user is not None:
            if form.is_valid():
                attendance = form.save(commit=False)
                attendance.user = user
                current_time = datetime.now().time()
                current_datetime = datetime.combine(datetime.today(), current_time)

                # Check late/early conditions
                if direction == "Check In":
                    check_in_time = time(9, 0, 0)  # 5:00 PM
                    check_in_datetime = datetime.combine(datetime.today(), check_in_time)
                    diff_check_in = current_datetime - check_in_datetime

                    # Convert timedelta to time if late
                    if diff_check_in.total_seconds() > 0:
                        late_time = (datetime.min + diff_check_in).time()
                        attendance.late_by = late_time
                    else:
                        attendance.late_by = None

                if direction == "Check Out":
                    check_out_time = time(18, 0, 0)  # 6:00 PM
                    check_out_datetime = datetime.combine(datetime.today(), check_out_time)
                    diff_check_out = check_out_datetime - current_datetime

                    # Convert timedelta to time if early
                    if diff_check_out.total_seconds() > 0:
                        early_time = (datetime.min + diff_check_out).time()
                        attendance.early_by = early_time
                    else:
                        attendance.early_by = None
                attendance.save()
                # login(self.request, user)

                messages.success(request, "Attendance recorded successfully!")
                return redirect("attendance")
            else:
                messages.error(request, "Invalid form submission.")
                return render(request, self.template_name, {"form": form})

        else:
            messages.error(request, "Username or password is incorrect.")
            return render(request, self.template_name, {"form": form})

class DeleteAttendanceView(USERloginRequiredMixin, View):
    def get(self, request, id):
        print(id)
        delete_query = get_object_or_404(Attendance, id=id)
        delete_query.is_delete = True
        delete_query.save()

        return redirect("home")

