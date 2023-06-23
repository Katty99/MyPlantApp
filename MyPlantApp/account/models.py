from django.core.validators import MinLengthValidator
from django.db import models

from MyPlantApp.account.validators import check_name_for_capital


# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=10, validators=[MinLengthValidator(2), ])
    first_name = models.CharField(max_length=20, validators=[check_name_for_capital, ])
    last_name = models.CharField(max_length=20, validators=[check_name_for_capital, ])
    profile_picture = models.URLField(blank=True, null=True)
