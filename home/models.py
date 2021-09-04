from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50,default="")
    email = models.EmailField(max_length=254,default="")
    phone = models.IntegerField(default=0)
    message = models.TextField(max_length=500,default="")

    def __str__(self):
        return self.email

class Patientinfo(models.Model):

    firstname = models.CharField(max_length=50,default="")
    lastname = models.CharField(max_length=50,default="")
    username = models.CharField(max_length=50,default="")
    email = models.EmailField(max_length=254,default="",unique=True)
    phone = models.IntegerField(default=0)
    gender = models.CharField(max_length=50,default="")
    report = models.FileField(upload_to='media',default=None)

    def __str__(self):
        return self.email