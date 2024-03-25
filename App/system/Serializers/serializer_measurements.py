from rest_framework import serializers
from ..Models.measurements import Measurements


class MeasurementSerializer(serializers.ModelSerializer):
    """
    Serializer for Measurement model
    """
    class Meta:
        fields = '__all__'
        model = Measurements
