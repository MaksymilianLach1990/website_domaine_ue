from django.shortcuts import render
from django.http import HttpResponse
from django.template import response
from .models import Domaine, Item
from .forms import CreateNewDomaine
# Create your views here.

def home(response):
    return render(response, "vineyards/home.html", {})

def vineyards(response):
    return render(response, "vineyards/vineyards.html", {})

def domains_list(response):
    domaine = Domaine.objects.all()
    if response.method == "POST":
        new_domaine = CreateNewDomaine(response.POST)

        if new_domaine.is_valid():
            n = new_domaine.cleaned_data["name"]
            d = Domaine(name=n)
            d.save()
        
        return render(response, "vineyards/domains_list.html", {"domaine":domaine, "new_domaine":new_domaine}) 
    else:
        new_domaine = CreateNewDomaine()
        return render(response, "vineyards/domains_list.html", {"domaine":domaine, "new_domaine":new_domaine}) 

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