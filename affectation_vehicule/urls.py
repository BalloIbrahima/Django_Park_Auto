from . import views
from django.urls import path

urlpatterns=[
    path('affectation_vehicule/',views.affectation_vehicule,name='affectation_vehicule')
]