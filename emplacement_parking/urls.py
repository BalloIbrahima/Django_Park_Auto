from . import views
from django.urls import path

urlpatterns=[
    path('emplacement_parking/',views.emplacement_parking,name='emplacement_parking')
]