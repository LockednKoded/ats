from django.db import models
from django import forms
from django.core.urlresolvers import reverse
from django.utils import timezone


# Create your models here.

class CargoManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(CargoManager, self).filter(approved_plan=True)




class cargo(models.Model):
    cargo_no = models.PositiveIntegerField(primary_key=True)
    cargo_airline = models.CharField(max_length=100)
    original = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    terminal = models.PositiveSmallIntegerField()
    weight = models.IntegerField(null=0)
    fare=models.IntegerField(null=weight)
    scheduled_arrival = models.DateField(auto_now=False, auto_now_add=False, null='15-07-2017')
    scheduled_departure = models.DateField( auto_now=False, auto_now_add=False,null='14-07-2017')
    objects = CargoManager()

    # need to be called objects for Cargo."objects".all or .active
   # def clean(self):
        # form.is_valid() returns False when ValidationError is raised and user can give correct details then
       # if self.scheduled_departure > self.scheduled_arrival:
          #  raise forms.ValidationError('Scheduled arrival should not be before scheduled departure')
      # if self.revised_departure < self.scheduled_departure:
           # raise forms.ValidationError('Scheduled departure should be before revised departure')
            # if self.scheduled_arrival < timezone.now or self.scheduled_departure < timezone.now:
            #     raise forms.ValidationError('Cannot set timings in the past')

    def __str__(self):
        return str(self.cargo_no)

    def get_absolute_url(self):
        # generating url that matches the specified url function name
        return reverse("cargo_info:view-cargo", kwargs={"pk": self.cargo_no})


   # def ___str__(self):
      #  return self.cargo_no + " - " + self.cargo_airline + " - " + self.weight

