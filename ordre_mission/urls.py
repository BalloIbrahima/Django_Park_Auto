from . import views
from django.urls import path

urlpatterns=[
    path('ordre_mission/',views.ordre_mission,name='ordre_mission')
]