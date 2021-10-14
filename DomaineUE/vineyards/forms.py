from django import forms


class CreateNewDomaine(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    region = forms.CharField(label="Region", max_length=200)
    vilage = forms.CharField(label="Vilage", max_length=200)
    text = forms.CharField(label="Text", max_length=250)
    check = forms.BooleanField()


class ContactMessage(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    text = forms.CharField(label="Text", max_length=500)
    email = forms.EmailField(label="Email", max_length=200)
