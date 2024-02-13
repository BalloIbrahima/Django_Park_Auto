from . import views
from django.urls import path

urlpatterns=[
    path('mission/',views.mission,name='mission')
]