from django.db import models

# Create your models here.

class Employers(models.Model):
    domaine = models.CharField(max_length=200)
    host_name = models.CharField(max_length=50)
    surname_host = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    region = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.objects.all()


class Workers(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    experience = models.TextField(max_length=250)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name, self.surname