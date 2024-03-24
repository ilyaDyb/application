from django.urls import path
from main import views

app_name = "main"

urlpatterns = [
    path("", view=views.index, name="index"),
    path("save-value/", view=views.save_value, name="save_value"),
    path("delete-data-from-cache/", view=views.delete_data_from_cache, name="delete_data_from_cache"),
    path("leaderboard/", view=views.leaderboard, name="leaderboard"),
    path("trade-score/", views.trade_score, name="trade_score"),
    path("convert-score/", views.convert_score, name="convert_score"),
]
