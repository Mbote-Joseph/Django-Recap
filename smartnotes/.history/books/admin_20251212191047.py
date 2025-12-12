from django.contrib import admin

from . import models

# Register your models here.
class BooksModel(admin.ModelAdmin):
    list_display = ("title","author",)
    
admin.site.register(models.Books)