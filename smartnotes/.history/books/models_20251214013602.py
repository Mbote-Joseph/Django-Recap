from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="books")
    
