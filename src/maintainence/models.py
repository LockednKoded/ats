from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Workers(models.Model) :
    WORKER_TYPES = (
        (0, 'Fueling'),
        (1, 'Cleaning'),
        (2, 'Cabin service'),
    )
    worker = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    worker_type = models.IntegerField(default=0, blank=True, choices=WORKER_TYPES)

@receiver(post_save, sender=User)
def create_worker_profile(sender, instance, created, **kwargs):
    if created:
        new_work_profile = Workers(user=instance)
        new_work_profile.save()
