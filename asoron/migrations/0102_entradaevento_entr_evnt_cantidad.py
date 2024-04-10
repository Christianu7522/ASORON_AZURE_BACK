# Generated by Django 4.2.8 on 2023-12-18 22:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0101_entradaevento'),
    ]

    operations = [
        migrations.AddField(
            model_name='entradaevento',
            name='entr_evnt_cantidad',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Cantidad'),
        ),
    ]
