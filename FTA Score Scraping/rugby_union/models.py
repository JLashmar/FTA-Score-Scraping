from django.db import models

# Create your models here.
'match_date', 'home_team', 'away_team'


class RFU_Fixtures(models.Model):
    #tournament_id = models.ForeignKey(PGA_Comp, on_delete=models.CASCADE)
    match_date = models.DateField(default=None, blank=True, null=True)
    home_team = models.CharField(max_length=200, default=None, blank=True, null=True)
    away_team = models.CharField(max_length=200, default=None, blank=True, null=True)

    def __str__(self):
        return "%s, %s v %s" % (self.match_date, self.home_team, self.away_team)


class RFU_Table(models.Model):
    #tournament_id = models.ForeignKey(PGA_Comp, on_delete=models.CASCADE)
    position = models.CharField(max_length=4, default='none', blank=True, null=True)
    team = models.CharField(max_length=200, default='none', blank=True, null=True)
    played = models.FloatField(null=True, blank=True)
    win = models.FloatField(null=True, blank=True)
    loss = models.FloatField(null=True, blank=True)
    draw = models.FloatField(null=True, blank=True)
    points_for = models.FloatField(null=True, blank=True)
    points_against = models.FloatField(null=True, blank=True)
    points_difference = models.FloatField(null=True, blank=True)
    try_bonus = models.FloatField(null=True, blank=True)
    loss_bonus = models.FloatField(null=True, blank=True)
    points = models.FloatField(null=True, blank=True)
