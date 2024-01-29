from django.contrib import admin

from departement.models import departement


# Register your models here.
class AdminDepartement(admin.ModelAdmin):
    list_display=['Nom_Departement']

admin.site.register(departement,AdminDepartement)
