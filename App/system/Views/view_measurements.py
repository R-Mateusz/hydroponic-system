from rest_framework import viewsets
from ..Serializers.serializer_measurements import MeasurementSerializer
from ..Models.measurements import Measurements
from rest_framework import permissions


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurements.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
