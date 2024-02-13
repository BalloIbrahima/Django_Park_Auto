from . import views
from django.urls import path

urlpatterns=[
    path('division/',views.division,name='division')
]