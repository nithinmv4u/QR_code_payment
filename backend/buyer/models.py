from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)
