from django.db import models
from django import forms
from django.core.urlresolvers import reverse
from django.utils import timezone


class security_forces(models.Model):
    name = models.CharField(max_length=100)
    license_no = models.PositiveIntegerField()


    def get_absolute_url(self):
        return reverse("security:view-security_forces", kwargs={"pk": self.license_no})


    def __str__(self):
        return self.name



class force_employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    force = models.ForeignKey(security_forces,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    experience = models.PositiveSmallIntegerField(default=0)
    license_no = models.PositiveIntegerField()
    ph_no = models.BigIntegerField()
    in_service = models.BooleanField(default=True)

    # blank=True --> There may be unassigned crew, Crew table doesn't have total participation
    # flights = models.ManyToManyField('flight_info.Flight', blank=True)


    def get_absolute_url(self):
        return reverse("security:view-force_employee", kwargs={"pk": self.employee_id})
