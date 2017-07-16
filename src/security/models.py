from django.db import models
from django import forms
from django.core.urlresolvers import reverse
from django.utils import timezone





class security_forces(models.Model):
    name = models.CharField(max_length=100)
    license_no = models.PositiveIntegerField()
    no_of_people = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name


# Need to instantiate these model managers in their respective classes
class SecurityManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(SecurityManager, self).filter(approved_plan=True)


class Flight(models.Model):
    flight_no = models.PositiveIntegerField(primary_key=True)
    airline = models.ForeignKey(security_forces)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    terminal = models.PositiveSmallIntegerField()
    concourse = models.PositiveSmallIntegerField()
    approved_plan = models.BooleanField(default=False)
    operation_days = models.CharField(max_length=13)  # eg. 1,0,1,0,1,0,0 for a flight (M,W,F)



    objects = SecurityManager()

    def __str__(self):
        return str(self.flight_no) + " - " + self.airline.name

    def get_absolute_url(self):
        # generating url that matches the specified url function name
        return reverse("security_info:view-flight", kwargs={"pk": self.flight_no})


# Need to instantiate these model managers in their respective classes
class security_commander(models.Manager):
    def active(self, *args, **kwargs):
        return super(security_commander, self).filter(in_service=True)


class force_employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    experience = models.PositiveSmallIntegerField(default=0)
    license_no = models.PositiveIntegerField()
    ph_no = models.BigIntegerField()
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    in_service = models.BooleanField(default=True)

    # blank=True --> There may be unassigned crew, Crew table doesn't have total participation
    flights = models.ManyToManyField(Flight, blank=True)

    objects = SecurityManager()



    def get_absolute_url(self):
        return reverse("security_info:view-force_employee", kwargs={"pk": self.employee_id})
