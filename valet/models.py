# valet/models.py
from django.db import models


class Vehicle(models.Model):
    ESTADO_CHOICES = [
        ("En Custodia", "En Custodia"),
        ("Devuelto", "Devuelto"),
    ]

    username = models.CharField(max_length=50)
    brand_model = models.CharField(max_length=100)
    key_code = models.CharField(max_length=20)
    ticket_number = models.CharField(max_length=20, unique=True)
    responsible = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=ESTADO_CHOICES, default="En Custodia")
    parking_spot = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticket_number} - {self.brand_model}"