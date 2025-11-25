from rest_framework import generics, permissions
from .models import SensorReading, AnomalyEvent, AgentRecommendation
from .serializers import (
    SensorReadingSerializer,
    AnomalyEventSerializer,
    AgentRecommendationSerializer
)

# POST /api/sensor-readings/
class SensorReadingCreateView(generics.CreateAPIView):
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingSerializer
    permission_classes = [permissions.AllowAny]


# GET /api/sensor-readings/list/?plot=<id>
class SensorReadingListView(generics.ListAPIView):
    serializer_class = SensorReadingSerializer

    def get_queryset(self):
        qs = SensorReading.objects.all().order_by("-timestamp")
        plot_id = self.request.query_params.get("plot")

        if plot_id:
            qs = qs.filter(plot__id=plot_id)

        return qs


class AnomalyListView(generics.ListAPIView):
    queryset = AnomalyEvent.objects.all().order_by("-timestamp")
    serializer_class = AnomalyEventSerializer


class RecommendationListView(generics.ListAPIView):
    queryset = AgentRecommendation.objects.all().order_by("-timestamp")
    serializer_class = AgentRecommendationSerializer
