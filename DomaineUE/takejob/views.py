from django.shortcuts import render
from .forms import CreateNewWorker, CreateNewEmployer
from .models import Workers

# Create your views here.

def registration(response):
    if response.method == "POST":
        new_worker = CreateNewWorker(response.POST)    

        if new_worker.is_valid():
            name = new_worker.cleaned_data["name"]
            surname = new_worker.cleaned_data["surname"]
            worker = Workers(name=name, surname=surname)
            worker.save()

    else:

        new_worker = CreateNewWorker()
        return render(response, "takejob/registration.html", {
            "form1":new_worker, 
            })

def conditions(response):
    return render(response, "takejob/conditions.html", {})

def for_employers(response):
    return render(response, "takejob/for_employer.html", {})

def for_workers(response):
    return render(response, "takejob/for_worker.html", {})

def jobs(response):
    return render(response, "takejob/jobs.html", {})