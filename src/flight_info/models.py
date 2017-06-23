
from django.db import models
from django.utils import timezone


class Flight(models.Model):
    flight_no = models.PositiveIntegerField(primary_key=True)
    airline = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    terminal = models.PositiveSmallIntegerField()
    concourse = models.PositiveSmallIntegerField()
    fare = models.FloatField()
    total_seats = models.PositiveIntegerField()
    booked_seats = models.PositiveIntegerField()
    operation_days = models.CommaSeparatedIntegerField(max_length=50)
    approved_plan = models.BooleanField(default=False)
    status_delayed = models.BooleanField(default=False)
    scheduled_arrival = models.DateTimeField(auto_now=False, auto_now_add=False)
    scheduled_departure = models.DateTimeField(auto_now=False, auto_now_add=False)
    revised_arrival = models.DateTimeField(auto_now=False, auto_now_add=False)
    revised_departure = models.DateTimeField(auto_now=False, auto_now_add=False)

    def ___str__(self):
        return self.flight_no


class Crew(models.Model):
    name = models.CharField(max_length=100)
    pilot = models.BooleanField(default=False)  # False for Crew, True for pilot
    crew_id = models.IntegerField(primary_key=True)
    experience = models.PositiveSmallIntegerField()
    license = models.PositiveIntegerField()
    ph_no = models.BigIntegerField()
    flight_link = models.ManyToManyField(Flight, blank=True)

    def ___str__(self):
        return self.name



