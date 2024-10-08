# Generated by Django 5.1 on 2024-08-26 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otrans', '0015_salary_month'),
        ('primary_setup', '0023_bank_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfitDistribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('financial_year', models.CharField(default='July-June', max_length=20)),
                ('year', models.CharField(max_length=9)),
                ('profit_type', models.CharField(max_length=50)),
                ('profit_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total_account', models.PositiveIntegerField()),
                ('profit_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('process_by', models.CharField(default='Admin', max_length=100)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primary_setup.branch')),
            ],
        ),
    ]
