from django.db import models

class Dvd(models.Model):
    """A DVD"""
    title = models.CharField(max_length=50)
    barcode = models.IntegerField()

    def __str__(self):
        return self.title