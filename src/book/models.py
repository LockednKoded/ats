# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Book(models.Model):
    Name = models.CharField(max_length=50)
    Room = models.CharField(max_length=50)
    check_in = models.DateTimeField(auto_now=False,auto_now_add=False)
    check_out = models.DateTimeField(auto_now=False,auto_now_add=False)
    contact_no = models.PositiveIntegerField()

    def __str__(self):
        return self.Name + " | " + self.contact_no







