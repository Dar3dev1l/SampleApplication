from django.db import models

AVAILABILITY_OPTIONS = {"YES", "NO"}


class Sports(models.Model):
    sport_name = models.CharField(max_length=50,null=True)
    max_players = models.IntegerField(default=0)
    min_players = models.IntegerField(default=0)
    team_sport = models.BooleanField(default=False)


class Area(models.Model):
    sport = models.ForeignKey(Sports, null=True, on_delete=models.SET_NULL)
    area = models.CharField(max_length=20)
    available = AVAILABILITY_OPTIONS


class Equipment(models.Model):
    sport = models.ForeignKey(Sports, null=True, on_delete=models.SET_NULL)
    equipment = models.CharField(max_length=50)
    available = AVAILABILITY_OPTIONS

