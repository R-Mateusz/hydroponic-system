from rest_framework import viewsets
from ..Serializers.serializer_hydroponic_system import HydroponicSystemSerializer
from ..Serializers.serializer_measurements import MeasurementSerializer
from ..Models.hydroponic_system import HydroponicSystem
from ..Models.measurements import Measurements
from rest_framework.response import Response

class HydroponicSystemViewSet(viewsets.ModelViewSet):
    serializer_class = HydroponicSystemSerializer
    queryset = HydroponicSystem.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        measurements = Measurements.objects.filter(system=instance).order_by('-id')[:10]
        measurements_serializer = MeasurementSerializer(measurements, many=True)
        data = serializer.data
        data['measurements'] = measurements_serializer.data
        return Response(data)

