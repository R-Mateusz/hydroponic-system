from rest_framework import serializers
from ..Models.measurements import Measurements


class MeasurementSerializer(serializers.ModelSerializer):
    """
    Serializer for Measurement model
    """
    class Meta:
        """
        class Meta for parent model
        """
        fields = '__all__'
        model = Measurements
