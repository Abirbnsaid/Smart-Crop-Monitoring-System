from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SensorReading
from .detectors import check_threshold_and_create

@receiver(post_save, sender=SensorReading)
def auto_detect(sender, instance, created, **kwargs):
    if created:
        check_threshold_and_create(instance)
