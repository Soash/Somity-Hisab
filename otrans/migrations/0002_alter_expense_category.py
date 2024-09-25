# Generated by Django 5.1 on 2024-08-16 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otrans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('electric_bill', 'Electric Bill'), ('guest_snack', 'Guest Snack'), ('wifi_bill', 'WiFi Bill'), ('staff_salary', 'Staff Salary'), ('bazar', 'Bazar'), ('house_rent', 'House Rent')], max_length=50),
        ),
    ]
