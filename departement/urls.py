from . import views
from django.urls import path

urlpatterns=[
    path('departement/',views.departement,name='departement')
]