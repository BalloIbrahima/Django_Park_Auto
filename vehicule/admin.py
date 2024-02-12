from django.contrib import admin

# Register your models here.
from vehicule.models import vehicule

# Register your models here.
class AdminVehicule(admin.ModelAdmin):
    list_display=['Immatriculation']

admin.site.register(vehicule,AdminVehicule)