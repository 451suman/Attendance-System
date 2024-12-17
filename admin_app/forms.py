from django import forms


class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())
    # is_valid = forms.BooleanField()
