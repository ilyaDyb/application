from django.shortcuts import redirect, render
from django.urls import reverse


def registration(request):
    return render(request, "user/registration.html")


def login(request):
    return render(request, "user/login.html")


def logout(request):
    return redirect(reverse("main:index"))