from django.urls import path
from main import views

app_name = "main"

urlpatterns = [
    path("", view=views.index, name="index"),
]
