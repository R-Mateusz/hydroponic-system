from django.db import models

class HydroponicSystem(models.Model):
    """
    Hydroponic system model that contains data from sensors
    """
    system_model = models.CharField(max_length=10, unique=True, null=False, default='XYZ')
    user = models.ForeignKey('auth.User', related_name='hydroponic_systems', on_delete=models.CASCADE)

    def __str__(self):
        """
        Gets the name of the system object
        :return: system_model
        """
        return self.system_model

    class Meta:
        verbose_name_plural = 'Hydroponic System'
