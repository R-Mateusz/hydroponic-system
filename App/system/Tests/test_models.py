from django.test import TestCase
from ..Models.hydroponic_system import HydroponicSystem
from django.contrib.auth.models import User

from django.urls import reverse


class HydroponicSystemTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_superuser(
            username='matiios2',
            password='123'
        )
        self.system = HydroponicSystem(system_model='ABC', user=self.test_user)
    def test_create(self):
        self.system.save()
        self.assertIsNotNone(self.system.id)
