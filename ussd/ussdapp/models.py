from django.db import models

# Create your models here.

class Detail(models.Model):
    firstname = models.Charfield(max_length=355)
    lastname = models.Charfield(max_length=244)
    phonenumber = models.IntegerField()
    age = models.IntegerField()

