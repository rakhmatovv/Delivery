from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    region1 = models.CharField(max_length=255)
    services= models.CharField(max_length=255)
def __str__(self):
    return self.name