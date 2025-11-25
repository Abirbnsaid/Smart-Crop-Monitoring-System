from datetime import timedelta
from .models import SensorReading, AnomalyEvent, AgentRecommendation

THRESHOLDS = {
    "moisture": {"min": 35, "drop_pct_hour": 10},
    "temperature": {"max": 32},
    "humidity": {"min": 30, "max": 85},
}

def check_threshold_and_create(reading):
    st = reading.sensor_type
    val = reading.value
    plot = reading.plot

    # Simple moisture threshold
    if st == "moisture" and val < THRESHOLDS["moisture"]["min"]:
        anomaly = AnomalyEvent.objects.create(
            plot=plot,
            anomaly_type="irrigation",
            severity=1.0,
            model_confidence=0.9,
            details={"value": val}
        )

        AgentRecommendation.objects.create(
            anomaly=anomaly,
            recommended_action="Arroser immédiatement (moisture très faible).",
            explanation_text=f"L'humidité ({val}%) est sous le seuil critique de 35%.",
            confidence=0.9
        )
