from django.db import models

class BandanaCondition(models.Model):
    name = models.CharField(max_length=100)
