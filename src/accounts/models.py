from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def content_file_name(instance):
    return ' - '.join([instance.user.username, 'photo'])


class BaseProfile(models.Model):
    USER_TYPES = (
        (0, 'No Type'),
        (1, 'Traveller'),
        (2, 'Employee'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_type = models.IntegerField(default=0, blank=True, choices=USER_TYPES)
    contact_no = models.BigIntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to=content_file_name, null=True, blank=True,
                              width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username + " - " + str(self.user_type)

    class Meta:
        abstract = True


class TravellerProfile(models.Model):
    ticket_no = models.IntegerField(null=True, blank=True)
    flight_no = models.ForeignKey('flight_info.Flight', null=True, blank=True)

    class Meta:
        abstract = True


class EmployeeProfile(models.Model):
    DESIGNATIONS = (
        (0, 'Small'),
        (1, 'Medium'),
        (2, 'High'),
        (3, 'Very High'),
    )
    DEPARTMENTS = (
        (0, 'Flight/Ticketing'),
        (1, 'Baggage Handling'),
        (2, 'Cargo Handling'),
        (3, 'Maintenance Services'),
        (4, 'Parking'),
        (5, 'Retiring Room'),
        (6, 'Security'),
        (7, 'HR'),
    )
    employee_id = models.IntegerField(null=True, blank=True)
    DOJ = models.DateField(null=True, blank=True)
    DOB = models.DateField(null=True, blank=True)
    designation = models.IntegerField(null=True, blank=True, choices=DESIGNATIONS)
    department = models.IntegerField(null=True, blank=True, choices=DEPARTMENTS)
    salary = models.FloatField(null=True, blank=True)

    class Meta:
        abstract = True


class Profile(BaseProfile, TravellerProfile, EmployeeProfile):
    pass


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        new_profile = Profile(user=instance)
        new_profile.save()


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
