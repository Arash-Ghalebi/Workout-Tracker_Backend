from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class BodyWeight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.name