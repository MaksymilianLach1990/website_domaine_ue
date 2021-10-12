from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def weather(response):
    return render(response, "maps/weather.html", {})

def points(response):
    return render(response, "maps/points.html", {})

def date_vintage(response):
    return render(response, "maps/date_vintage.html", {})

