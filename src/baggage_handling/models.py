from django.db import models
from django.core.urlresolvers import reverse


class BaggageHandling(models.Model):
    pnr_no = models.CharField(max_length=6)
    quantity = models.PositiveSmallIntegerField()
    weight = models.FloatField()
    conveyor_no = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.pnr_no + ' - ' + str(self.conveyor_no) + " - " + str(self.pk)

    def get_absolute_url(self):
        return reverse("baggage_handling:view-baggage", kwargs={'pk':self.pk})

