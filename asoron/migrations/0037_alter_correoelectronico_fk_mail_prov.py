# Generated by Django 4.2.7 on 2023-11-13 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asoron', '0036_correoelectronico_fk_mail_prov'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correoelectronico',
            name='fk_mail_prov',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='asoron.proveedor'),
        ),
    ]
