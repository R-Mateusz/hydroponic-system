from django.test import TestCase
from django.urls import reverse

class HydroponicSystemTest(TestCase):
    def test_view_systems(self):
        url = reverse('HydroponicSystemViewSet')
        response = self.client.get(url, format='json')
        self.assertEquals(response.status_code, status=200)

class MeasurementsTest(TestCase):

    def test_post_measurement(self):
        data = {
        'system_hydroponic':'ABC',
        'measurement': 101010,
        'ph': 10.1,
        'water_temperature': 10.1,
        'tds': 10.1
        }

        url = reverse('measurement-create')
        response = self.client.post(url,data, format='json')

        self.assertEquals(response, status=201)
