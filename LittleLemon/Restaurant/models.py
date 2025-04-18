from django.db import models

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    noOfGuests = models.IntegerField()
    bookingDate = models.DateTimeField()


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

