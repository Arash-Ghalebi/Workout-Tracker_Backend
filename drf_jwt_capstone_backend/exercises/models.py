from django.db import models

class Exercise(models.Model):
    exercise_name = models.CharField(max_length=50)

    def __str__(self):
        return self.exercise_name