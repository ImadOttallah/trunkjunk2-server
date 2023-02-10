from django.db import models
from .bandana_pattern import BandanaPattern
from .bandana_color import BandanaColor
from .bandana_marking import BandanaMarking
from .bandana_condition import BandanaCondition
from .user import User

class Bandana(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    origin = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pattern = models.ForeignKey(BandanaPattern, on_delete=models.CASCADE)
    marking = models.ForeignKey(BandanaMarking, on_delete=models.CASCADE)
    color = models.ForeignKey(BandanaColor, on_delete=models.CASCADE)
    condition = models.ForeignKey(BandanaCondition, on_delete=models.CASCADE)
     
