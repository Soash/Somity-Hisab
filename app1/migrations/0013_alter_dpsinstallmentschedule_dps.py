# Generated by Django 5.1 on 2024-08-19 08:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_dpsinstallmentschedule_installment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dpsinstallmentschedule',
            name='dps',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dps_installment_schedules', to='app1.dps'),
        ),
    ]
