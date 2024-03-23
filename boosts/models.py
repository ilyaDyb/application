from django.db import models

from user.models import User


class Boosts(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    tap_ability = models.IntegerField(default=0)
    auto_click = models.IntegerField(default=0)
