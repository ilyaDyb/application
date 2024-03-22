from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from user.models import User

class RegistrationForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with such an email already exists")
        return email
    
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]