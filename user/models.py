from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    groups = models.ManyToManyField("auth.Group", related_name="custom_user_set")
    user_permissions = models.ManyToManyField("auth.Permission", related_name="custom_user_set")
    score = models.BigIntegerField(default=0)
    tap_ability = models.IntegerField(default=1)
    auto_click = models.IntegerField(default=0)
    miner = models.IntegerField(default=0)
    end_game = models.BooleanField(default=False)
    balance = models.DecimalField(default=0, max_digits=11, decimal_places=6)
    
    class Meta:
        db_table = "user"

    def __str__(self):
        return self.username
    