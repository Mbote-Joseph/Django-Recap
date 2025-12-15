from django.contrib import admin
from .models import ClassRoom
# Register your models here.

class AdminClassRoom(admin.ModelAdmin):
    list_display = ('name', 'stream')
    

admin.site.register(ClassRoom, AdminClassRoom)