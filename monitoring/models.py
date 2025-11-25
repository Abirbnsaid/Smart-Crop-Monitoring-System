from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class FarmProfile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="farms")
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)
    size = models.FloatField(null=True, blank=True)
    crop_type = models.CharField(max_length=100, blank=True, null=True)

class FieldPlot(models.Model):
    farm = models.ForeignKey(FarmProfile, on_delete=models.CASCADE, related_name="plots")
    name = models.CharField(max_length=200)
    crop_variety = models.CharField(max_length=100, blank=True, null=True)

class SensorReading(models.Model):
    SENSOR_CHOICES = [
        ("moisture","moisture"),
        ("temperature","temperature"),
        ("humidity","humidity"),
    ]
    timestamp = models.DateTimeField()
    plot = models.ForeignKey(FieldPlot, on_delete=models.CASCADE, related_name="readings")
    sensor_type = models.CharField(max_length=30, choices=SENSOR_CHOICES)
    value = models.FloatField()
    source = models.CharField(max_length=100, default="simulator")

class AnomalyEvent(models.Model):
    ANOMALY_TYPES = [
        ("irrigation","irrigation"),
        ("temperature","temperature"),
        ("humidity","humidity"),
        ("other","other"),
    ]
    timestamp = models.DateTimeField(auto_now_add=True)
    plot = models.ForeignKey(FieldPlot, on_delete=models.CASCADE, related_name="anomalies")
    anomaly_type = models.CharField(max_length=50, choices=ANOMALY_TYPES)
    severity = models.FloatField(null=True, blank=True)
    model_confidence = models.FloatField(null=True, blank=True)
    details = models.JSONField(default=dict, blank=True)

class AgentRecommendation(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    anomaly = models.ForeignKey(AnomalyEvent, on_delete=models.CASCADE, related_name="recommendations")
    recommended_action = models.TextField()
    explanation_text = models.TextField()
    confidence = models.FloatField(null=True, blank=True)
