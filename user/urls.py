from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path("registration/", views.registration, name="registration"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]
