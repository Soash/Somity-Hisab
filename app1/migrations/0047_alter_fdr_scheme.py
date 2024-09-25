# Generated by Django 5.1 on 2024-08-22 08:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0046_fdr_duration'),
        ('primary_setup', '0020_alter_customuser_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fdr',
            name='scheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fdrs', to='primary_setup.dpsscheme'),
        ),
    ]