from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import auth

from user.forms import UserLoginForm, RegistrationForm
from user.models import User


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("user:login"))
    else:
        form = RegistrationForm()
    
    return render(request, "user/registration.html", context={"form":form})


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]

            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                return redirect(reverse("main:index"))
    else:
        form = UserLoginForm()

    return render(request, "user/login.html", context={"form":form})


def logout(request):
    auth.logout(request)
    return redirect(reverse("main:index"))