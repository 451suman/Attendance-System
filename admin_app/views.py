from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from admin_app.forms import AdminLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin




# class AdminLoginView(FormView):
#     template_name = 'admin/authentication/admin_login.html'
#     form_class = AdminLoginForm
#     success_url = reverse_lazy('a_app:admin-home')

#     def form_validate(self, form):
#         username = form.cleaned_data["username"]
#         password = form.cleaned_data["password"]
        
#         admin_user = authenticate(username=username, password=password)
#         if admin_user is not None:
#             if admin_user.is_superuser:  # Check if the user is a superuser
#                 print("---------------------------------------------------------")
#                 print(username)
#                 print(password)
#                 print("---------------------------------------------------------")  
#                 messages.success(self.request, "Welcome Admin!")
#                 login(self.request, admin_user)
#             else:
#                 messages.error(self.request, "You are not authorized to login here")
#                 return redirect('a_app:admin-login')

#         else:
#             messages.error(self.request, "Username or password is incorrect")
#             return redirect('a_app:admin-login')
#         return super().form_validate(form)

class AdminLoginView(FormView):
    template_name = "admin/authentication/admin_login.html"
    form_class = AdminLoginForm
    success_url = reverse_lazy("a_app:admin-home")

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
                messages.success(self.request, "You dont have permission to access this website!")
                return render(
                    self.request,
                    self.template_name,
                    {"form": self.form_class, "error": "Invalid credentials"},
            )

        else:
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
            return redirect('a_app:admin-login')  # Redirect to login page if not authorized

        return super().dispatch(request, *args, **kwargs)



class AdminHomeView(AdminloginRequiredMixin, TemplateView):
    template_name = "admin/home/home.html"

