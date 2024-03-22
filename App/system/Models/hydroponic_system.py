from django.db import models
class HydroponicSystem(models.Model):
    """
    Hydroponic system model that contains data from sensors
    """
    system_model = models.CharField(max_length=10, unique=True, null=False, default='XYZ')

    def __str__(self):
        return self.system_model

    class Meta:
        """
        inner Meta class for HydroponicSystem
        """
        verbose_name_plural = 'Hydroponic System'


