from django.db import models

AVAILABILITY_OPTIONS = ("YES", "NO")


class Sport(models.Model):
    sport_name = models.CharField(max_length=50,null=True)
    max_players = models.IntegerField(default=0)
    min_players = models.IntegerField(default=0)
    team_sport = models.BooleanField(default=False)

    def __str__(self):
        return self.sport_name


class Area(models.Model):
    sport = models.ForeignKey(Sport, null=True, on_delete=models.SET_NULL)
    area = models.CharField(max_length=20)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.area


class Equipment(models.Model):
    sport = models.ForeignKey(Sport, null=True, on_delete=models.SET_NULL)
    equipment = models.CharField(max_length=50)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.equipment
