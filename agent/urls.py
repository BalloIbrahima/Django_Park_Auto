from . import views
from django.urls import path

urlpatterns=[
    path('agent/',views.agent,name='agent')
]