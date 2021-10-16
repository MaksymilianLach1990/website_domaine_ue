from django import forms

class CreateNewWorker(forms.Form):
    name = forms.CharField(label="Name", max_length=50)
    surname = forms.CharField(label="Surname", max_length=50)
    email = forms.EmailField(label="Email")
    experiense = forms.CharField(label="Experiense", max_length=250)
    description = forms.CharField(label="Description", max_length=300)


class CreateNewEmployer(forms.Form):
    domaine_name = forms.CharField(label="Domaine", max_length=200)
    name = forms.CharField(label="Name", max_length=50)
    surname = forms.CharField(label="Surname", max_length=50)
    email = forms.EmailField(label="Email")
    region = forms.CharField(label="Region", max_length=200)
    vilage = forms.CharField(label="Vilage", max_length=200)
    description = forms.CharField(label="Description", max_length=500)



