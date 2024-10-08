# Generated by Django 5.1 on 2024-08-16 19:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otrans', '0003_income'),
        ('primary_setup', '0017_dpsscheme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processed_by', models.CharField(blank=True, max_length=50, null=True)),
                ('Date', models.DateField()),
                ('VoucherID', models.CharField(editable=False, max_length=50, unique=True)),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Note', models.CharField(blank=True, max_length=200, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primary_setup.branch')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primary_setup.director')),
            ],
        ),
    ]
