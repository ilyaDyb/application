from django.urls import path
from main import views

app_name = "main"

urlpatterns = [
    path("", view=views.index, name="index"),
    path("save-value/", view=views.save_value, name="save_value"),
    path("delete-data-from-cache/", view=views.delete_data_from_cache, name="delete_data_from_cache"),
]
