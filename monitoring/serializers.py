from rest_framework import serializers
from .models import FarmProfile, FieldPlot, SensorReading, AnomalyEvent, AgentRecommendation

class FarmProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmProfile
        fields = "__all__"


class FieldPlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldPlot
        fields = "__all__"


class SensorReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorReading
        fields = "__all__"

    # Exemple de validation basique
    def validate(self, data):
        st = data.get("sensor_type")
        value = data.get("value")

        if st == "moisture" and not (0 <= value <= 100):
            raise serializers.ValidationError("Moisture must be between 0 and 100")

        return data


class AnomalyEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnomalyEvent
        fields = "__all__"


class AgentRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentRecommendation
        fields = "__all__"
