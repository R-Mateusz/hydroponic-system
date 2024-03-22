from rest_framework import serializers
from ..Models.hydroponic_system import HydroponicSystem


class HydroponicSystemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = HydroponicSystem


