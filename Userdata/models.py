from django.db import models
from django.contrib import auth

# Create your models here.
class UserInput(models.Model):
    number = models.PositiveIntegerField(blank=False)
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name


