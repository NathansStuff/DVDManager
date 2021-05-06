from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

class ModelTests(TestCase):
    
    def test_create_dvd(self):
        """Test creating a new dvd is successful"""
        dvd = models.Dvd.objects().create(
            barcode = 12345,
            title = 'Hunger Games'
        )

        self.assertEqual(str(title), dvd.title)