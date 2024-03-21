from django.db import models
class Measurements(models.Model):
    """
    Measurements from sensors
    """
    measurement = models.IntegerField(unique=True, null=False, default=1)
    ph = models.DecimalField(decimal_places=1, max_digits=5, null=False, default=10.0)
    water_temperature = models.DecimalField(decimal_places=1, max_digits=5, null=False, default=20.0)
    tds = models.DecimalField(decimal_places=1, max_digits=5, null=False, default=10.0)

    def __str__(self):
        return str(self.measurement)

    class Meta:
        """
        inner Meta class for Measurements
        """
        verbose_name_plural = 'Measurement'