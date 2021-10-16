from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.

def registration(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/domaine/")
    else:
        form = RegisterForm()
    
    return render(response, "user/registration.html", {"form":form})
