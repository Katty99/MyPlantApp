from django import template
from MyPlantApp.plant_app.models import PlantApp

register = template.Library()


@register.filter(name="price_filter")
def price_filter(price):
    return "%.2f" % price
