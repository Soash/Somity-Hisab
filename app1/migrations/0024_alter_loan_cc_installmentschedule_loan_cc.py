# Generated by Django 5.1 on 2024-08-20 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0023_rename_scheme_loan_cc_loan_scheme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan_cc_installmentschedule',
            name='loan_cc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_cc_installment_schedules', to='app1.loan_cc'),
        ),
    ]
