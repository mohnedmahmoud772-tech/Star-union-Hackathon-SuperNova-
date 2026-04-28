from django.db import models


class ExtraFood(models.Model):
    provider = models.ForeignKey(
        "registration_and_login.Provider", on_delete=models.CASCADE
    )
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    quantity_unit = models.CharField(max_length=50)
    shelf_life = models.DurationField()

    STATUS_CHOICES = [
        ("NO_RECEIVER", "No Receiver"),
        ("NO_DELIVERY", "No Delivery"),
        ("WAITING_FOR_DELIVERY", "Waiting For Delivery"),
        ("ON_THE_WAY_TO_RECEIVER", "On The Way To Receiver"),
        ("DONE", "Done"),
        ("FAILED", "FAILED"),
        ("EXPIRED", "Expired"),
    ]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="NO_RECEIVER")
    
    def __str__(self):
        return self.description
