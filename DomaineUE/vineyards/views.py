from django.shortcuts import render
from django.http import HttpResponse
from django.template import response
from .models import Domaine, Item
# Create your views here.

def home(response):
    return render(response, "vineyards/home.html", {})

def vineyards(response):
    return render(response, "vineyards/vineyards.html", {})

def domains_list(response):
    domaine = Domaine.objects.all()
    indexy = []
    for item in domaine:
        if item.id % 2 == 0:
            indexy.append(0)
        else:
            indexy.append(1)

    return render(response, "vineyards/domains_list.html", {"domaine":domaine, "index": indexy}) 

def domaine_detals(response, id):
    domaine = Domaine.objects.get(id=id)
    return render(response, "vineyards/domaine_detals.html", {"domaine":domaine})

def work(response):
    return render(response, "vineyards/work.html", {})

def spring_season(response):
    return render(response, "vineyards/spring_season.html", {}) 

def winter_season(response):
    return render(response, "vineyards/winter_season.html", {})

def vintage(response):
    return render(response, "vineyards/vintage.html", {})

def contact(response):
    return render(response, "vineyards/contact.html", {})