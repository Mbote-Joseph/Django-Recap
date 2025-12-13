from django.db import models

# Create your models here.

class Animal(models.Model):
    LOCATIONS = {
        ('savannah', 'Savannah'),
        ('jungle', 'Jungle'),
        ('ocean', 'Ocean'),
        ('desert', 'Desert'),
    }
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    location = models.CharField(max_length=100, choices=LOCATIONS)

    # def __str__(self):
    #     return f"{self.name} the {self.species}"