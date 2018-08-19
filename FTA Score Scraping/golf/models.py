from django.db import models


class PGA_Comp(models.Model):
    tournament_name = models.CharField(max_length=200, default='none', blank=True, null=True)
    start_date = models.DateField(default=None, blank=True, null=True)
    end_date = models.DateField(default=None, blank=True, null=True)
    location = models.CharField(max_length=200, default=None, blank=True, null=True)
    par_total = models.IntegerField(default=None, blank=True, null=True)
    distance_total = models.IntegerField(default=None, blank=True, null=True)
    purse_total = models.CharField(max_length=200, default=None, blank=True, null=True)
    champ = models.CharField(max_length=200, default=None, blank=True, null=True)
