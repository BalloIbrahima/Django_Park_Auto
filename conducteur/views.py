from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def conducteur(request):
    return HttpResponse("Hello world conducteur")