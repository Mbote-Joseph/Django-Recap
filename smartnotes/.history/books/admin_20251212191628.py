from django.contrib import admin

from . import models

# Register your models here.
class BooksAdmin(admin.ModelAdmin):
    list_display = ("title","author",)
    
admin.site.register(models.Books, BooksAdmin)