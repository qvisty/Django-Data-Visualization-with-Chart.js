from calendar import day_abbr
from django.db import models


# Create your models here.
class CountryData(models.Model):
    country = models.CharField(max_length=100)
    population = models.IntegerField()

    class Meta:
        verbose_name_plural = "Country Population Data"

    def __str__(self):
        return f"{self.country}-{self.population}"


class Freetime(models.Model):
    name = models.CharField(max_length=100)
    days = models.IntegerField()
    department = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Freetimes"

    def __str__(self):
        return f"{self.department}:{self.name}-{self.days}"


from django.db import models
from django import forms


class Employee(models.Model):
    days = models.IntegerField()
    firstName = models.CharField(max_length=150, null=True)
    department = models.CharField(max_length=100, default="", blank=True, null=True)

    def __str__(self):
        return self.firstName

    objects = models.Manager()
