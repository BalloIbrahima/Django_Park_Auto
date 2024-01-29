from django.contrib import admin

from division.models import division

# Register your models here.
class AdminDivision(admin.ModelAdmin):
    list_display=['Nom_Division']

admin.site.register(division,AdminDivision)