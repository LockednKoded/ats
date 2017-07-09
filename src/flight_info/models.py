from django.db import models
from django import forms


class FlightManager(models.Manager):

    def active(self, *args, **kwargs):
        return super(FlightManager, self).filter(approved_plan=True)


class Airline(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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
    # need to be called objects for Flight."objects".all or .active

    def clean(self):
        # form.is_valid() returns False when ValidationError is raised and user can give correct details then
        if self.revised_arrival < self.scheduled_arrival:
            raise forms.ValidationError('Scheduled arrival should be before revised arrival')
        if self.revised_departure < self.scheduled_departure:
            raise forms.ValidationError('Scheduled departure should be before revised departure')

    def __str__(self):
        return str(self.flight_no) + " - " + self.airline.name


def content_file_name(instance):
    return ' - '.join([instance.crew_id, "photo"])


class Crew(models.Model):
    crew_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    pilot = models.BooleanField(default=False)  # False for Crew, True for pilot
    experience = models.PositiveSmallIntegerField(default=0)
    license_no = models.PositiveIntegerField()
    ph_no = models.BigIntegerField()
    photo = models.ImageField(upload_to=content_file_name, null=True, blank=True,
                              width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    # blank=True --> There may be unassigned crew, Crew table doesn't have total participation
    flights = models.ManyToManyField(Flight, blank=True)

    def ___str__(self):

        if self.pilot:
            return self.crew_id + " " + self.name + " - " + "Pilot"
        else:
            return self.crew_id + " " + self.name + " - " + "Crew"
