from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def mission(request):
    return HttpResponse("Hello world mission")