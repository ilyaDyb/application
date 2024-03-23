from django.urls import path

from boosts import views

app_name = "boosts"

urlpatterns = [
    path("", views.index, name="index"),
    path("buy_ability", views.buy_ability, name="buy_ability"),
]
