from django.contrib import admin
from reparation.models import reparation

# Register your models here.
class AdminReparation(admin.ModelAdmin):
    list_display=['Description_Panne']

admin.site.register(reparation,AdminReparation)