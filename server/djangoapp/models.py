from django.db import models
from django.utils.timezone import now
import datetime


# Create your models here.

# CarMake model
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default="")
    description = models.CharField(null=False, max_length=30, default="")
    
    
    # Create a toString method for object string representation
    def __str__(self):
        return f"{self.name} {self.description}"


# CarModel class: Many-To-One relationship to CarMake Model

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE, default="")
    dealerId = models.IntegerField(null=False, default=1)
    car_model = models.CharField(null=False, max_length=30,default="")
    
    TYPE_CHOICE = (
        ('SEDAN', 'sedan'), 
        ('SUV','suv'),
        ('WAGON','wagon'),
        )
    
    YEAR_CHOICES = []
    for r in range(1990, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r, r))
        
    car_type = models.CharField(null=False, max_length=30, choices=TYPE_CHOICE) 
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)

    # Create a toString method for object string representation
    def __str__(self):
        return f"{self.car_make} {self.car_model} {self.dealerId} {self.year} {self.car_type}"


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
        return "Dealer name: " + self.short_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment
        self.id = id

    def __str__(self):
        return "Review id: " + str(self.id)