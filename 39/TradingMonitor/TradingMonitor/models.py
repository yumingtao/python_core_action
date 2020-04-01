from django.db import models


class Position(models.Model):
    asset = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=3)
