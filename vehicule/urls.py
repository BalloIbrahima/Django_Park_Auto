from . import views
from django.urls import path

urlpatterns=[
    path('vehicule/',views.vehicule,name='vehicule')
]