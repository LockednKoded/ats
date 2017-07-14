from django.db import models
from django import forms
from django.core.urlresolvers import reverse
from django.utils import timezone


def airline_img_path(instance, filename):
    path = '-'.join(["airline", str(instance.id), "logo", filename])
    return path


class Airline(models.Model):
    name = models.CharField(max_length=100)
    flight_prefix = models.CharField(max_length=5)
    license_no = models.PositiveIntegerField()
    no_of_aircrafts = models.PositiveIntegerField(default=0)
    logo = models.ImageField(upload_to=airline_img_path, null=True, blank=True,
                             width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("flight_info:view-airlines", kwargs={"pk": self.id})


# Need to instantiate these model managers in their respective classes
class FlightManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(FlightManager, self).filter(approved_plan=True)


class Flight(models.Model):
    flight_no = models.PositiveIntegerField(primary_key=True)
    airline = models.ForeignKey(Airline)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    terminal = models.PositiveSmallIntegerField()
    concourse = models.PositiveSmallIntegerField()
    fare = models.FloatField()
    total_seats = models.PositiveIntegerField()
    booked_seats = models.PositiveIntegerField(default=0)
    approved_plan = models.BooleanField(default=False)
    operation_days = models.CharField(max_length=13)  # eg. 1,0,1,0,1,0,0 for a flight (M,W,F)

    # Time attributes
    scheduled_arrival = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    scheduled_departure = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    revised_arrival = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    revised_departure = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    time_last_updated = models.DateField(auto_now_add=True)

    objects = FlightManager()

    def __str__(self):
        return str(self.flight_no) + " - " + self.airline.name

    def get_absolute_url(self):
        # generating url that matches the specified url function name
        return reverse("flight_info:view-flight", kwargs={"pk": self.flight_no})


# Need to instantiate these model managers in their respective classes
class CrewManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(CrewManager, self).filter(in_service=True)


def crew_img_path(instance, filename):
    path = '-'.join(["crew", str(instance.crew_id), "photo", filename])
    return path


class Crew(models.Model):
    crew_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    pilot = models.BooleanField(default=False)  # False for Crew, True for pilot
    experience = models.PositiveSmallIntegerField(default=0)
    license_no = models.PositiveIntegerField()
    ph_no = models.BigIntegerField()
    photo = models.ImageField(upload_to=crew_img_path, null=True, blank=True,
                              width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    in_service = models.BooleanField(default=True)

    # blank=True --> There may be unassigned crew, Crew table doesn't have total participation
    flights = models.ManyToManyField(Flight, blank=True)

    objects = CrewManager()

    def __str__(self):

        if self.pilot:
            return str(self.crew_id) + " " + self.name + " - " + "Pilot"
        else:
            return str(self.crew_id) + " " + self.name + " - " + "Crew"

    def get_absolute_url(self):
        return reverse("flight_info:view-crew", kwargs={"pk": self.crew_id})
