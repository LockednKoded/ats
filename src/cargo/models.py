from django.db import models


# Create your models here.
class Cargo(models.Model):
    cargo_no = models.PositiveIntegerField(primary_key=True)
    cargo_airline = models.CharField(max_length=100)
    original = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    terminal = models.PositiveSmallIntegerField()
    fare = models.FloatField()
    weight=models.FloatField()

    def ___str__(self):
        return self.cargo_no + " - " + self.cargo_airline + " - " + self.weight

