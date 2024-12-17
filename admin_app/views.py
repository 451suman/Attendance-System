from django.shortcuts import render
from django.views import View

from admin_app.forms import AdminLoginForm
# Create your views here.


class AdminLoginView(View):
    def get(self, request):
        form = AdminLoginForm()
        return render(request, "admin/authentication/login.html", {"form": form})
