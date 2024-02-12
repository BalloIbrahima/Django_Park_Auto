from django.contrib import admin

from affectation_vehicule.models import affectationvehicule
# Register your models here.
class AdminAffectationVehicule(admin.ModelAdmin):
    list_display=['ID_Emplacement']

admin.site.register(affectationvehicule,AdminAffectationVehicule)