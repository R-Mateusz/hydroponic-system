from django.db import models


class HydroponicSystem(models.Model):
    """
    Hydroponic system model that contains data from sensors
    """
    system_model = models.CharField(max_length=10, unique=True, null=False, default='XYZ')
    ph = models.DecimalField(decimal_places=1, max_digits=5, null=False, default=10.0)
    water_temperature = models.DecimalField(decimal_places=1, max_digits=5, null=False, default=20.0)
    tds = models.DecimalField(decimal_places=1, max_digits=5, null=False, default=10.0)

    def __str__(self):
        return self.system_model
    class Meta:
        """
        inner Meta class for System model
        """
        verbose_name_plural = 'Hydroponic System'