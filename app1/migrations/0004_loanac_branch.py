# Generated by Django 5.1 on 2024-08-18 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_loanac_loan_scheme'),
        ('primary_setup', '0020_alter_customuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanac',
            name='branch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='primary_setup.branch'),
        ),
    ]
