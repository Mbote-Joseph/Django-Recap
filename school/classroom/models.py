from django.db import models

# Create your models here.
class ClassRoom(models.Model):
    FOCUS_AREA = {
        ('Sciences', 'Sciences'),
        ('Sports', 'Sports'),
        ('Languages', 'Languages'),
    }
    
    STREAM = {
        ('Red', 'Red'),
        ('Green', 'Green'),
        ('Blue', 'Blue'),
        ('Yellow', 'Yellow'),
    }
    COLOR = {
        ('Black', 'Black'),
        ('Grey', 'Grey'),
        ('White', 'White')
    }
    name = models.CharField(max_length=100)
    stream = models.CharField(max_length=100, choices= STREAM)
    focus = models.CharField(max_length=100, choices=FOCUS_AREA)
    students = models.IntegerField()
    uniform = models.CharField(max_length=100, choices=COLOR)
    classteacher = models.CharField(max_length=100)
    
    