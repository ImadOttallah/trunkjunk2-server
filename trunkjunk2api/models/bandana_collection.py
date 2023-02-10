from django.db import models
from .bandana import Bandana
from .collection import Collection

class BandanaCollection(models.Model):
    bandana = models.ForeignKey(Bandana, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
