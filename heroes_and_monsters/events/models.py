from django.db import models
from entities.models import Hero, Villain

class Event(models.Model):
    name = models.CharField(max_length=255)
    participating_heroes = models.ManyToManyField(Hero)
    participating_villains = models.ManyTomanyField(Villain)
