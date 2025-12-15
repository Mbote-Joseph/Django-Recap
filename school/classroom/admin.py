from django.contrib import admin
from .models import ClassRoom
# Register your models here.

class AdminClassRoom(admin.ModelAdmin):
    list_display = ('name', 'stream', 'focus', 'students', 'uniform', 'classteacher')
    search_fields = ('name', 'stream', 'focus', 'students', 'uniform', 'classteacher')
    
    

admin.site.register(ClassRoom, AdminClassRoom)