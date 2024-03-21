from django.contrib import admin
from .Models.system import HydroponicSystem

class SystemAdmin(admin.ModelAdmin):
    """
    SystemAdmin class for System model
    """
    fields = ['system_model', 'ph', 'water_temperature','tds']

    list_display = [f"{field}" for field in fields]


admin.site.register(HydroponicSystem)


