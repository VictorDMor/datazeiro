from __future__ import unicode_literals

from django.db import models

class Country(models.Model):
	name = models.CharField(max_length=100)
	abbreviation = models.CharField(max_length=3)

class Player(models.Model):
	first_name = models.CharField(max_length=200)
	second_name = models.CharField(max_length=200)
	known_as = models.CharField(max_length=200)
	age = models.IntegerField(default=0)
	nationality = models.ForeignKey(Country, on_delete=models.CASCADE)
	goals = models.IntegerField(default=0)
	assists = models.IntegerField(default=0)
	height = models.IntegerField(default=0)
	weight = models.IntegerField(default=0)