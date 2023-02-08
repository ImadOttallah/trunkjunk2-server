from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
