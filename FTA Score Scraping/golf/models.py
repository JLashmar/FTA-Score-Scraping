from django.db import models


class PGA_Comp(models.Model):
    tournament_name = models.CharField(max_length=200, default='none', blank=True, null=True)
    start_date = models.DateField(default=None, blank=True, null=True)
    end_date = models.DateField(default=None, blank=True, null=True)
    location = models.CharField(max_length=200, default=None, blank=True, null=True)
    par_total = models.IntegerField(default=None, blank=True, null=True)
    distance_total = models.CharField(max_length=200, default=None, blank=True, null=True)
    purse_total = models.CharField(max_length=200, default=None, blank=True, null=True)
    champ = models.CharField(max_length=200, default=None, blank=True, null=True)


class PGA_Event(models.Model):
    tournament_id = models.ForeignKey(PGA_Comp, on_delete=models.CASCADE)
    position = models.CharField(max_length=4, default='none', blank=True, null=True)
    name = models.CharField(max_length=200, default='none', blank=True, null=True)
    to_par = models.CharField(max_length=4, default='none', blank=True, null=True)
    current_round = models.CharField(max_length=4, default='none', blank=True, null=True)
    thru = models.CharField(max_length=20, default='none', blank=True, null=True)
    round1 = models.CharField(max_length=4, default='none', blank=True, null=True)
    round2 = models.CharField(max_length=4, default='none', blank=True, null=True)
    round3 = models.CharField(max_length=4, default='none', blank=True, null=True)
    round4 = models.CharField(max_length=4, default='none', blank=True, null=True)
    total_score = models.CharField(max_length=4, default='none', blank=True, null=True)
