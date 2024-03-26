from django.db import models
from .hydroponic_system import HydroponicSystem


class Measurements(models.Model):
    """
    Measurements from sensors
    """
    system_hydroponic = models.ForeignKey(HydroponicSystem, on_delete=models.CASCADE, null=True,
                                          related_name='measurements')
    measurement = models.IntegerField(unique=True, null=False, default=1)
    ph = models.DecimalField(decimal_places=1, max_digits=5, null=False, default=11.0)
    water_temperature = models.DecimalField(decimal_places=1, max_digits=5, null=False, default=20.0)
    tds = models.DecimalField(decimal_places=1, max_digits=5, null=False, default=10.0)

    def __str__(self):
        """
        Gets the name of measurement object
        :return: measurement
        """
        return str(self.measurement)

    class Meta:
        verbose_name_plural = 'Measurement'
