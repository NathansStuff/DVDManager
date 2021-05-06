from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Dvd
from core.serializers import DvdSerializer

DVDS_URL + reverse('dvd:list')

class DvdApiTests(TestCase):
    """Test the DVD API"""

    def test_retrieve_dvds_info(self):
        """Test retrieving a dvds info"""
        Dvd.objects.create(
            barcode = 12345,
            title = 'Harry Potter'
        )
        Dvd.objects.create(
            barcode = 23456,
            title = 'Naruto'
        )

        res = self.client.get(DVDS_URL)
        dvds = Dvd.objects.all()
        serializer = DvdSerializer(dvds, many=true)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)