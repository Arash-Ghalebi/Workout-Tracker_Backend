from email.policy import default
from django.db import models
from django.conf import settings
from exercises.models import Exercise

User = settings.AUTH_USER_MODEL


class ExerciseActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, default=None)
    weight_amount = models.IntegerField()
    weight_date = models.DateField()

    def __str__(self):
        return self.name