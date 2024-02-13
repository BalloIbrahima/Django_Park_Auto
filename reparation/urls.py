from . import views
from django.urls import path

urlpatterns=[
    path('reparation/',views.reparation,name='reparation')
]