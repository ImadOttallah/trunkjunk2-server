from django.db import models

class BandanaColor(models.Model):
    name = models.CharField(max_length=50)
