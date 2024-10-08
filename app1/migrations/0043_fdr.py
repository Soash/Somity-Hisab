# Generated by Django 5.1 on 2024-08-22 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0042_savingsac_savingsdeposit_savingstransactionhistory_and_more'),
        ('primary_setup', '0020_alter_customuser_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='FDR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starte_date', models.DateField()),
                ('end_date', models.DateField()),
                ('opening_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('balance_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_profit', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('paid_profit', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('available_profit', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('transaction_id', models.CharField(editable=False, max_length=15, unique=True)),
                ('processed_by', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('closed', 'Closed')], default='active', max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.customer')),
                ('scheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primary_setup.dpsscheme')),
            ],
        ),
    ]
