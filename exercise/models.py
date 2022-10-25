from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Exercise(models.Model):
    exercise = models.CharField(max_length=255, blank=True)
    intensity = models.CharField(max_length=255, blank=True)
    duration = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(default=datetime.now())
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.exercise