from django.db import models
from django.contrib.auth.models import User

class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    establishment_name = models.CharField(max_length=255)
    # ACTIVITY_TYPE_CHOICES = [
    #     ('restaurant', 'Restaurant'),
    #     ('bakery', 'Bakery'),
    #     ('hotel', 'Hotel'),
    #     ('other', 'Other'),
    # ]
    # activity_type = models.CharField(max_length=50, choices=ACTIVITY_TYPE_CHOICES)
    activity_type = models.CharField(max_length=50)
    
    commercial_registration_number = models.CharField(max_length=100, unique=True)
    
    # WE SHOULD STORE GEOGRAPHICAL LOCATION ON THE MAP INSTEAD OF THIS
    address = models.TextField()
    
    person_in_charge_full_name = models.CharField(max_length=255)
    
    person_in_charge_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.establishment_name


class Receiver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    entity_name = models.CharField(max_length=255)
    
    registration_license_number = models.CharField(max_length=100, unique=True)
    
    # WE SHOULD STORE GEOGRAPHICAL LOCATION ON THE MAP INSTEAD OF THIS
    address = models.TextField()
    
    person_in_charge_full_name = models.CharField(max_length=255)
    
    person_in_charge_phone = models.CharField(max_length=20)

    def __str__(self):
        return self.person_in_charge_full_name


class Volunteer(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    full_name = models.CharField(max_length=255)
    
    national_id_number = models.CharField(max_length=20, unique=True)
    
    # TRANSPORT_CHOICES = [
    #     ('car', 'Car'),
    #     ('bike', 'Bike'),
    #     ('other', 'Other'),
    # ]
    # means_of_transportation = models.CharField(max_length=50, choices=TRANSPORT_CHOICES)
    means_of_transportation = models.CharField(max_length=50)
    
    # This should be an array of addresses instead of this
    addresses = models.TextField()  
    
    def __str__(self):
        return self.full_name
