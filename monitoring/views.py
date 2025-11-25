from rest_framework import generics, permissions
from .models import SensorReading, AnomalyEvent, AgentRecommendation, FarmProfile, FieldPlot
from .serializers import (
    SensorReadingSerializer, AnomalyEventSerializer, 
    AgentRecommendationSerializer, FarmProfileSerializer, FieldPlotSerializer
)

# === VUES POUR TOUT LE MONDE (sans auth) ===
class SensorReadingCreateView(generics.CreateAPIView):
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingSerializer
    permission_classes = [permissions.AllowAny]  # ← Simulateur peut poster sans auth

class SensorReadingListView(generics.ListAPIView):
    serializer_class = SensorReadingSerializer
    permission_classes = [permissions.AllowAny]  # ← Temporaire pour tests

    def get_queryset(self):
        qs = SensorReading.objects.all().order_by("-timestamp")
        plot_id = self.request.query_params.get("plot")
        if plot_id:
            qs = qs.filter(plot__id=plot_id)
        return qs

class AnomalyListView(generics.ListAPIView):
    queryset = AnomalyEvent.objects.all().order_by("-timestamp")
    serializer_class = AnomalyEventSerializer
    permission_classes = [permissions.AllowAny]  # ← Temporaire pour tests

class RecommendationListView(generics.ListAPIView):
    queryset = AgentRecommendation.objects.all().order_by("-timestamp")
    serializer_class = AgentRecommendationSerializer
    permission_classes = [permissions.AllowAny]  # ← Temporaire pour tests

# === VUES AVEC AUTHENTIFICATION (pour plus tard) ===
class FarmProfileListCreateView(generics.ListCreateAPIView):
    queryset = FarmProfile.objects.all()
    serializer_class = FarmProfileSerializer
    permission_classes = [permissions.IsAuthenticated]  # ← Auth requis

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)