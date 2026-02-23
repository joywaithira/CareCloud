from django.db import models

# Create your models here.
class patient(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    dateregistered = models.DateTimeField()
    medicalhistory = models.TextField()


def __str__(self):
    return self.firstname + self.lastname