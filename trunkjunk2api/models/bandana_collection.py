from django.db import models
from .bandana import Bandana
from .collection import Collection

class BandanaCollection(models.Model):
    bandana = models.ForeignKey(Bandana, on_delete=models.CASCADE, related_name="joined_bandanas")
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('bandana', 'collection')
