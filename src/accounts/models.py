from django.db import models
from django.conf import settings

# Create your models here.


def content_file_name(instance, filename):
    return ' - '.join([instance.user.username, filename])


class BaseProfile(models.Model):
    USER_TYPES = (
        (0, 'Traveller'),
        (1, 'Employee'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    # this will change in Django 2.0
    # primary_key=True, to deal with concurrency issues in PostGRE
    # can write User in place of settings.AUTH_USER_MODEL

    user_type = models.IntegerField(max_length=1, null=True, blank=True, choices=USER_TYPES)
    contact_no = models.BigIntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to=content_file_name, null=True, blank=True,
                              width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return self.user + " - " + self.user_type

    class Meta:
        abstract = True


class TravellerProfile(models.Model):
    traveller_id = models.IntegerField(null=True, blank=True)
    # ticket_no

    class Meta:
        abstract = True


class EmployeeProfile(models.Model):
    JOB_POSTS = (
        (0, 'Small'),
        (1, 'Medium'),
        (2, 'High'),
        (3, 'Very High')
    )

    DEPARTMENTS = (
        (0, 'Flight/Ticketing'),
        (1, 'Baggage Handling'),
        (2, 'Cargo Handling'),
        (3, 'Maintainence Services'),
        (4, 'Parking'),
        (5, 'Retiring Room'),
        (6, 'Security'),
        (7, 'HR'),
    )

    employee_id = models.IntegerField(null=True, blank=True)
    DOJ = models.DateField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    designation = models.IntegerField(max_length=1, null=True, blank=True, choices=JOB_POSTS)
    department = models.IntegerField(max_length=1, null=True, blank=True, choices=DEPARTMENTS)
    salary = models.FloatField(null=True, blank=True)

    class Meta:
        abstract = True


class Profile(TravellerProfile, EmployeeProfile, BaseProfile):
    pass

#  All signals have been written in signals.py
