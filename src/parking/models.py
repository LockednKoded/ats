# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
# Create your models here.


class VehicleDetail(models.Model):
    VEH_TYPES = (
        (2, '2-wheeler(Motorcycle/Scooter)'),
        (3, '3-wheeler(Auto)'),
        (4, '4-wheeler(Car/Bus)'),
    )
    vehicle_no = models.CharField(max_length=12, primary_key=True)
    vehicle_type = models.IntegerField(choices=VEH_TYPES)
    date = models.DateField()
    time_in = models.TimeField()
    time_out = models.TimeField()

    def __str__(self):
        return self.vehicle_no


class ParkingSpot(models.Model):
    spots_available = models.IntegerField(default=0)
    spots_occupied = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Parking Spots [updated: " + self.last_updated.strftime('%d-%m-%Y %H:%M:%S') + " ]"
