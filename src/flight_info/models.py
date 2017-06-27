
from django.db import models


class Flight(models.Model):
    flight_no = models.PositiveIntegerField(primary_key=True)
    airline = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    terminal = models.PositiveSmallIntegerField()
    concourse = models.PositiveSmallIntegerField()
    fare = models.FloatField()
    total_seats = models.PositiveIntegerField()
    booked_seats = models.PositiveIntegerField(default=0)
    approved_plan = models.BooleanField(default=False)
    operation_days = models.CharField(max_length=13)  # eg. 1,0,1,0,1,0,0 for a flight (M,W,F)
    status_delayed = models.BooleanField(default=False)

    # Time attributes
    scheduled_arrival = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    scheduled_departure = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    revised_arrival = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    revised_departure = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    time_last_updated = models.DateField(auto_now_add=True)

    def ___str__(self):
        return self.flight_no + " - " + self.airline


class Crew(models.Model):
    crew_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    pilot = models.BooleanField(default=False)  # False for Crew, True for pilot
    experience = models.PositiveSmallIntegerField(default=0)
    license_no = models.PositiveIntegerField()
    ph_no = models.BigIntegerField()

    # blank=True --> There may be unassigned crew, Crew table doesn't have total participation
    flights = models.ManyToManyField(Flight, blank=True)

    def ___str__(self):

        if self.pilot:
            return self.crew_id + " " + self.name + " - " + "Pilot"
        else:
            return self.crew_id + " " + self.name + " - " + "Crew"