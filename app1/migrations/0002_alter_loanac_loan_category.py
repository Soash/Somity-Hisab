# Generated by Django 5.1 on 2024-08-16 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
        ('primary_setup', '0017_dpsscheme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanac',
            name='loan_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='primary_setup.loancategory'),
        ),
    ]