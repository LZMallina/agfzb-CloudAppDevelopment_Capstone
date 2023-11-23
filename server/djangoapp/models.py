from django.db import models
from django.utils.timezone import now


# Create your models here.

# CarMake model
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(null=False, max_length=30)
    
    
    # Create a toString method for object string representation
    def __str__(self):
        return "Name: " + self.name + "," + \
            "Description: " + self.description


# CarModel class: Many-To-One relationship to CarMake Model

class CarModel(models.Model):
    carmodel = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    dealerId = models.IntegerField(null=False)
    name = models.CharField(null=False, max_length=30)
    TYPE_CHOICE = (
        ('SEDAN', 'sedan'), 
        ('SUV','suv'),
        ('WAGON','wagon'),
        )
    type = models.CharField(null=False, max_length=30, choices=TYPE_CHOICE) 
    
    # Create a toString method for object string representation
    def __str__(self):
        return "Name: " + self.name + "," + \
            "Type: " + self.type + "," + \
            "DealerId: " + str(self.dealerId)


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
