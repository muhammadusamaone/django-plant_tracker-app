from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    watering_date = models.DateField()

    def __str__(self):
        return self.name
