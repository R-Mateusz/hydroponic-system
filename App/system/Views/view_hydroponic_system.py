from rest_framework import viewsets
from ..Serializers.serializer_hydroponic_system import HydroponicSystemSerializer
from ..Serializers.serializer_measurements import MeasurementSerializer
from ..Models.hydroponic_system import HydroponicSystem
from ..Models.measurements import Measurements
from rest_framework.response import Response
from ..permissions import Owner


class HydroponicSystemViewSet(viewsets.ModelViewSet):
    """
    ViewSet for HydroponicSystem model
    """
    serializer_class = HydroponicSystemSerializer
    queryset = HydroponicSystem.objects.all()
    permission_classes = [Owner]

    def get_queryset(self) -> queryset[HydroponicSystem]:
        """
        Returns list of objects related to the user
        :return: queryset[HydroponicSystem]
        """
        return HydroponicSystem.objects.filter(user=self.request.user)

    def retrieve(self, request, *args, **kwargs) -> Response:
        """
        Returns measurements for hydroponic system model based on a filter
        :param request: request
        :param args: *args
        :param kwargs: **kwargs
        :return: Response
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        measurements = Measurements.objects.filter(system_hydroponic=instance).order_by('-id')[:10]
        measurements_serializer = MeasurementSerializer(measurements, many=True)
        data = serializer.data
        data['measurements'] = measurements_serializer.data
        return Response(data)
