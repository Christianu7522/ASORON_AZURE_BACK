# Generated by Django 4.2.8 on 2023-12-17 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0098_evento_fk_event_tien_delete_inventarioevento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fk_event_tien',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='asoron.tienda', verbose_name='Tienda'),
        ),
    ]
