from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_datetime = models.DateTimeField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} - {self.origin} a {self.destination}'


