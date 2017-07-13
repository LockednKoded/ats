from django.db import models


class BaggageHandling(models.Model):
    pnr_no = models.CharField(max_length=6)
    quantity = models.PositiveSmallIntegerField()
    weight = models.FloatField()
    conveyor_no = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.pnr_no + ' - ' + str(self.conveyor_no)

