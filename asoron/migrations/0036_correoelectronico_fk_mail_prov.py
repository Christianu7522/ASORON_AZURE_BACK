# Generated by Django 4.2.7 on 2023-11-13 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0035_correoelectronico'),
    ]

    operations = [
        migrations.AddField(
            model_name='correoelectronico',
            name='fk_mail_prov',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='asoron.proveedor'),
        ),
    ]
