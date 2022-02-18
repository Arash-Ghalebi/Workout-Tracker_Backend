from django.db import models

from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Events(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.name