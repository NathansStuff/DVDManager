from django.db import models

class Model(models.Model):
    """A DVD"""
    title = models.CharField(max_length=50)
    barcode = models.IntegerField()

    def __str__(self):
        return self.title