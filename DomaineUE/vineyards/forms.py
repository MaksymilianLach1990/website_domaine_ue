from django import forms


class CreateNewDomaine(forms.Form):
    name = forms.CharField(lable="Name", max_length=200)