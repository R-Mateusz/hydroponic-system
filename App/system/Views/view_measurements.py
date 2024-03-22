from rest_framework.generics import CreateAPIView
from ..Serializers.serializer_measurements import MeasurementSerializer
from ..Models.measurements import Measurements
from ..Models.hydroponic_system import HydroponicSystem


class MeasurementCreateAPIView(CreateAPIView):
    serializer_class = MeasurementSerializer
    queryset = Measurements.objects.all()

