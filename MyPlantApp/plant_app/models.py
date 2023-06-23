from django.core.validators import MinLengthValidator
from django.db import models

from MyPlantApp.plant_app.validators import plant_name_validator

# Create your models here.
type_of_plant = [
    ('outdoor plants', 'Outdoor Plants'),
    ('indoor plant', 'Indoor Plants')
]


class PlantApp(models.Model):
    plant_type = models.CharField(max_length=14, choices=type_of_plant)
    name = models.CharField(max_length=20, validators=[MinLengthValidator(2, ), plant_name_validator])
    image_url = models.URLField()
    description = models.TextField()
    price = models.FloatField()
