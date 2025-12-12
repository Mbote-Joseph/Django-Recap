from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
