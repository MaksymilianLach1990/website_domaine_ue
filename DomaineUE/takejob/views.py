from django.shortcuts import render

# Create your views here.

def registration(response):
    return render(response, "takejob/registration.html")

def conditions(response):
    return render(response, "takejob/conditions.html")

def for_employers(response):
    return render(response, "takejob/for_employer.html")

def for_workers(response):
    return render(response, "takejob/for_worker.html")

def jobs(response):
    return render(response, "takejob/jobs.html")