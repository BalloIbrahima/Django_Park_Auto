"""
URL configuration for my_park_auto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

import division

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('division.urls')),
    # path('',include('mission.urls')),
    path('',include('affectation_vehicule.urls')),
    path('',include('agent.urls')),
    # path('',include('conducteur.urls')),
    # path('',include('departement.urls')),
    # path('',include('emplacement_parking.urls')),
    # path('',include('ordre_mission.urls')),
    # path('',include('reparation.urls')),
    # path('',include('vehicule.urls')),
    
    # path('',include('division.urls')),
    # path('',include('division.urls')),
    # path('',include('division.urls')),
    # path('',include('division.urls')),
    # path('',include('division.urls')),
    # path('',include('division.urls')),

]
