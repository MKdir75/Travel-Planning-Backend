from django.db import models

class Trip(models.Model):
    destination = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    hotel = models.CharField(max_length=100, blank=True, null=True)
    transport = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.destination
    
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Transport(models.Model):
    type = models.CharField(max_length=50)  # e.g. Bus, Train, Flight
    company = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.type} - {self.company}"

