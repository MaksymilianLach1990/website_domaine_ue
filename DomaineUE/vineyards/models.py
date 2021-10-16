from django.db import models

# Create your models here.

class Domaine(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)
    region = models.CharField(max_length=200)
    vilage = models.CharField(max_length=200)
    complete = models.BooleanField()

    def __str__(self):
        return self.region, self.vilage


class HelpMessage(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    contact = models.EmailField(max_length=200)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title, self.text, self.contact, self.post_date
