from django.contrib import admin

# Register your models here.
from ordre_mission.models import ordremission
# Register your models here.
class AdminOrdreMission(admin.ModelAdmin):
    list_display=['Description']

admin.site.register(ordremission,AdminOrdreMission)