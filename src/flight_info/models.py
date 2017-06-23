
from django.db import models
from django.utils import timezone

class Flights(models.Model):
    flight_no = models.PositiveIntegerField()
    airline = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    terminal = models.PositiveSmallIntegerField()
    concourse = models.PositiveSmallIntegerField()
    fare = models.FloatField()
    capacity = models.PositiveIntegerField()
    booked_seats =  models.PositiveIntegerField()
    operation_days = models.CommaSeparatedIntegerField()
    approved_plan = models.BooleanField(default=False)

    def ___str__(self):
        return self.title

class Crew(models.Model):
    name = models.CharField()
    pilot_or_crew = models.BooleanField()  #False for Crew, True for pilot
    id = models.IntegerField()
    experience = models.PositiveSmallIntegerField()
    license = models.PositiveIntegerField()
    ph_no = models.BigIntegerField()

    def ___str__(self):
        return self.title

class Time(models.Model):
    flight_no = models.ForeignKey(Flight)
    status_delayed =
    scheduled_arrival =
    scheduled_departure =
    revised_arrival =
    revised_departure =

    def ___str__(self):
        return self.title

class FlightAandCrew(models.Model):
    flight_no =
    crew_id =



    def ___str__(self):
        return self.title



