# Generated by Django 5.1 on 2024-08-20 12:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_loan_special'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan_Special_Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Date', models.DateField(blank=True, null=True)),
                ('Note', models.CharField(blank=True, max_length=200, null=True)),
                ('VoucherID', models.CharField(blank=True, editable=False, max_length=50, null=True, unique=True)),
                ('processed_by', models.CharField(blank=True, max_length=50, null=True)),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_sp_collection', to='app1.loan_special')),
            ],
        ),
    ]
