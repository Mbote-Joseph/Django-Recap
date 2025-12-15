from django.contrib import admin
from .models import ClassRoom
# Register your models here.

class AdminClassRoom(admin.ModelAdmin):
    pass

admin.site.register(ClassRoom, AdminClassRoom)