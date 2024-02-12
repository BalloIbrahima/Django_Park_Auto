from django.contrib import admin
from conducteur.models import conducteur

# Register your models here.
class AdminConducteur(admin.ModelAdmin):
    list_display=['Numero_Telephone']

admin.site.register(conducteur,AdminConducteur)