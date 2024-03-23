from django.urls import path, include
from rest_framework import routers
from .Views.view_measurements import MeasurementCreateAPIView
from .Views.view_hydroponic_system import HydroponicSystemViewSet

router = routers.DefaultRouter()
router.register(r'systems', HydroponicSystemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('measurements/', MeasurementCreateAPIView.as_view()),
    path('app-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
