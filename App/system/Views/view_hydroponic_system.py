from rest_framework import viewsets
from ..Serializers.serializer_hydroponic_system import HydroponicSystemSerializer
from ..Models.hydroponic_system import HydroponicSystem
from rest_framework import permissions

class HydroponicSystemViewSet(viewsets.ModelViewSet):
    queryset = HydroponicSystem.objects.all()
    serializer_class = HydroponicSystemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
