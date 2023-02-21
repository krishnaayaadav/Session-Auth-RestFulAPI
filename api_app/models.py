from django.db import models

# Create your models here.

class User(models.Model):
    name   =  models.CharField(max_length=100)
    email  =  models.EmailField(unique=True)
    message=  models.TextField()
    profession = models.CharField(max_length=50)

