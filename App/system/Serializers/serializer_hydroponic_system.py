from rest_framework import serializers
from ..Models.hydroponic_system import HydroponicSystem


class HydroponicSystemSerializer(serializers.ModelSerializer):
    """
    Serializer for HydroponicSystem model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        fields = '__all__'
        model = HydroponicSystem
