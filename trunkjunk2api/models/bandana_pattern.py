from django.db import models

class BandanaPattern(models.Model):
    name = models.CharField(max_length=100)
