from rest_framework.generics import CreateAPIView
from ..Serializers.serializer_measurements import MeasurementSerializer
from ..Models.measurements import Measurements


class MeasurementCreateAPIView(CreateAPIView):
    """
    CreateAPIView for Measurement model
    """
    serializer_class = MeasurementSerializer
    queryset = Measurements.objects.all()
