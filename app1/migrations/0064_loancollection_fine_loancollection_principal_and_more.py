# Generated by Django 5.1 on 2024-08-25 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0063_dps_dps_closing_charge_alter_dps_dps_opening_charge'),
    ]

    operations = [
        migrations.AddField(
            model_name='loancollection',
            name='fine',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='loancollection',
            name='principal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='loancollection',
            name='profit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='loancollection',
            name='Amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]