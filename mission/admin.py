from django.contrib import admin
from mission.models import mission

# Register your models here.
class AdminMission(admin.ModelAdmin):
    list_display=['Description']

admin.site.register(mission,AdminMission)