# Generated by Django 5.1 on 2024-08-18 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primary_setup', '0018_customuser_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
