from django.db import models
from .bandana_collection import BandanaCollection
from .user import User
class Collection(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    bandanaCollection = models.ForeignKey(BandanaCollection, on_delete=models.CASCADE)
