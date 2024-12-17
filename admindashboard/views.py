from urllib import request
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView,ListView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from admindashboard.forms import AdminLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin

from attendance_app.models import Attendance
from django.contrib.auth.models import User


class AdminLoginView(FormView):
    template_name = "admindashboard/authentication/admindashboard_login.html"
    form_class = AdminLoginForm
    success_url = reverse_lazy("a_app:admin-dashboard-home")

    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        print("------------------------------------------------------")
        print("------------------------------------------------------")
        print(uname)
        print(pword)
        print("------------------------------------------------------")
        print("------------------------------------------------------")

        if usr is not None:
            # Check if user is superuser or admin
            if usr.is_superuser:
                messages.success(self.request, "Welcome Admin!")
                login(self.request, usr)
                return super().form_valid(form)  # Redirect to success URL
            else:
                messages.error(self.request, "You dont have permission to access this website!")
                return render(
                    self.request,
                    self.template_name,
                    {"form": self.form_class, "error": "Invalid credentials"},
            )

        else:
            messages.error(self.request, "Invalid username and password!")

            return render(
                self.request,
                self.template_name,
                {"form": self.form_class, "error": "Invalid credentials"},
            )

class AdminloginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            pass
        else:
            return redirect('a_app:admin-dashboard-login')  # Redirect to login page if not authorized

        return super().dispatch(request, *args, **kwargs)



class AdminHomeView(AdminloginRequiredMixin, TemplateView):
    template_name = "admindashboard/home/home.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["users"] = User.objects.filter(is_staff = False).order_by("username")
        return context



# class AttendanceListuser(ListView):
#     template_name = "admindashboard/user_attendance/user_attendance.html"
#     model = Attendance
#     context_object_name = "attendances"

#     def get_queryset(self, pk):
#         queryset = super().get_queryset()
#         queryset = queryset.objects.filter(user=pk).order_by("-id")
#         return queryset


class AttendanceListuser(View):
    template_name = "admindashboard/user_attendance/user_attendance.html"
    model = Attendance

    def get(self, request, *args, **kwargs):
        u_id = kwargs["pk"]
        print(u_id)
        attendances = Attendance.objects.filter(user=u_id).order_by("-time")
        return render(request, self.template_name, {'attendances': attendances})

