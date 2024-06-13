from django.db import models
#from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Car Make Model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year_made = models.IntegerField()

    def __str__(self):
        return self.name


# Car Model Model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    horsepower = models.IntegerField()
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('ELECTRIC', 'Electric')
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2023,
                               validators=[
                                   MaxValueValidator(2023),
                                   MinValueValidator(2015)
                                   ])

    def __str__(self):
        return self.name
