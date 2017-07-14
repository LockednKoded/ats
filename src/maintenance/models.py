from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Worker(models.Model):
    WORKER_TYPES = (
        (0, 'No Type'),
        (1, 'Fuelling'),
        (2, 'Cleaning'),
        (3, 'Cabin Services'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    worker_type = models.IntegerField(default=0, blank=True, choices=WORKER_TYPES)


# This creates the associated worker model when a User model is created
@receiver(post_save, sender=User)
def create_worker_model(sender, instance, created, **kwargs):
    if created:
        new_worker = Worker(user=instance)
        new_worker.save()
