from django.contrib import admin
from .models import ClassRoomModel
# Register your models here.

class AdminClassRoomModel(admin.ModelAdmin):
    pass

admin.site.register(ClassRoomModel, AdminClassRoomModel)