from django.db import models

# Create your models here.

from django.db import models

class CSVData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()

    def __str__(self):
        return self.name

    
class RegisterUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name