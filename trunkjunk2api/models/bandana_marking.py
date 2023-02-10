from django.db import models

class BandanaMarking(models.Model):
    name = models.CharField(max_length=100)
