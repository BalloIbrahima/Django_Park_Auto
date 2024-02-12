from django.contrib import admin

from emplacement_parking.models import emplacement_parking
# Register your models here.
class AdminEmplacementParking(admin.ModelAdmin):
    list_display=['Nom_Emplacement']

admin.site.register(emplacement_parking,AdminEmplacementParking)