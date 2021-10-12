from django.db import models

# Create your models here.

class Domaine(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)
    region = models.CharField(max_length=200)
    adres = models.CharField(max_length=200)
    complete = models.BooleanField()

    def __str__(self):
        return self.region
