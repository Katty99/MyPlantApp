# Generated by Django 4.2.2 on 2023-06-20 12:51

import MyPlantApp.account.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)])),
                ('first_name', models.CharField(max_length=20, validators=[MyPlantApp.account.validators.check_name_for_capital])),
                ('last_name', models.CharField(max_length=20, validators=[MyPlantApp.account.validators.check_name_for_capital])),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
