# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.


class Album(models.Model):
    Room = models.CharField(max_length=50)
    check_in = models.CharField(max_length=250)
    check_out = models.CharField(max_length=250)
    duration = models.CharField(max_length=250)
    amt = models.CharField(max_length=250)






