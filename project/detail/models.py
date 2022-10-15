from django.db import models

# Create your models here.
class Patient(models.Model):
    fullname = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname

class Doctor(models.Model):
    fullname = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)
    upload_image = models.ImageField() 

    def __str__(self):
        return self.fullname
