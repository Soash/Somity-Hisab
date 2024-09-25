# Generated by Django 5.1 on 2024-08-19 12:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_dpsdeposit'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DPSWithdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(blank=True, null=True)),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Note', models.CharField(blank=True, max_length=200, null=True)),
                ('Give_Profit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VoucherID', models.CharField(blank=True, editable=False, max_length=50, null=True, unique=True)),
                ('dps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dps_withdrawals', to='app1.dps')),
                ('processed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]