# Generated by Django 5.1 on 2024-08-23 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0056_profithistory_current_balance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dps',
            name='dps_scheme',
        ),
    ]