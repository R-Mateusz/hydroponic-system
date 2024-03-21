from django.contrib import admin
from .Models.hydroponic_system import HydroponicSystem
from .Models.measurements import Measurements

class SystemAdmin(admin.ModelAdmin):
    """
    SystemAdmin class for System model
    """
    fields = ['system_model']

    list_display = [f"{field}" for field in fields]

class MeasurementAdmin(admin.ModelAdmin):
    """
    SystemAdmin class for System model
    """
    fields = ['measurement','ph', 'water_temperature','tds']

    list_display = [f"{field}" for field in fields]



admin.site.register(HydroponicSystem)
admin.site.register(Measurements)


