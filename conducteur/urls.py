from . import views
from django.urls import path

urlpatterns=[
    path('conducteur/',views.conducteur,name='conducteur')
]