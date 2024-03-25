from django.test import TestCase
from django.urls import reverse
from rest_framework import status

class HydroponicSystemTest(TestCase):
    def test_view_systems(self):
        url = reverse('systems')
        response = self.client.get(url, format='json')
        self.assertEquals(response.status_code, status=200)

class MeasurementsTest(TestCase):

    def test_post_measurement(self):
        data = {
        'system_hydroponic':2,
        'measurement': 10410,
        'ph': 10.1,
        'water_temperature': 10.1,
        'tds': 10.1
        }

        url = reverse('measurements')
        response = self.client.post(url,data, format='json')

        self.assertTrue(response.status_code, status.HTTP_200_OK)
