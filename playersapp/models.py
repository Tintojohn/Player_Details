from django.db import models

# Create your models here.
class Players(models.Model):
    Players_Id = models.IntegerField()
    Player_Name = models.CharField(max_length=100)
    Player_Email = models.EmailField(max_length=100)
    Country = models.CharField(max_length=100)
    Game = models.CharField(max_length=100)
    Score = models.IntegerField()
class meta:
    db_table = "playersdb"
