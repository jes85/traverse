from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=200)
    popularity = models.IntegerField(default=0)

class Location(models.Model):
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    latitude = models.IntegerField(default=0)
    longitude = models.IntegerField(default=0)

class Trip(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE) # maybe change on_delete to another option
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    cost = models.FloatField(default=0) # todo: derive the cost from other info (e.g. flight cost, driving cost, etc)
    rating = models.IntegerField(default=0)
    distance = models.FloatField(default=0) # temporary placeholder for distance todo: derive distance from location + current location

#todos: trip dates, seasonal trip info/ratings
