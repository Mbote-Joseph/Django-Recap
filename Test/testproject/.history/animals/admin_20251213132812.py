from django.contrib import admin
from .models import Animal

# Register your models here.
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'age', 'location')
    search_fields = ('name', 'species', 'age', 'location')
    list_filter = ('location',)
    
admin.site.register(Animal, AnimalAdmin)