from django.db import models

# Create your models here.

class Competition(models.Model):
    name = models.CharField(max_length=200, default="name")
    location = models.CharField(max_length=200, default=None, blank=True, null=True)
    club = models.CharField(max_length=200, default=None, blank=True, null=True)
    start_date = models.DateField(default=None, blank=True, null=True)
    end_date = models.DateField(default=None, blank=True, null=True)
    level = models.CharField(max_length=200, default=None, blank=True, null=True)
    tournament_type = models.CharField(max_length=200, default=None, blank=True, null=True)
    ranking = models.CharField(max_length=200, default=None, blank=True, null=True)
    winner_points = models.IntegerField(default=None, blank=True, null=True)
    finalist_points = models.IntegerField(default=None, blank=True, null=True)
    semi_points = models.IntegerField(default=None, blank=True, null=True)
    appearance_points = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return "%s" % (self.name)

class Result(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, default=None, blank=True, null=True)
    team_a = models.CharField(max_length=200)
    team_a_score = models.CharField(max_length=200, default=None, blank=True, null=True)
    team_b = models.CharField(max_length=200)
    team_b_score = models.CharField(max_length=200, default=None, blank=True, null=True)
    game_date = models.DateTimeField(default=None, blank=True, null=True)
