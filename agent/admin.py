from django.contrib import admin

# Register your models here.
from agent.models import agent
# Register your models here.
class AdminAgent(admin.ModelAdmin):
    list_display=['Numero_Telephone']

admin.site.register(agent,AdminAgent)