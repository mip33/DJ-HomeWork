# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer

class SensorViewSet(ModelViewSet):
    """ViewSet для проекта."""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementViewSet(ModelViewSet):
    """ViewSet для измерения."""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer