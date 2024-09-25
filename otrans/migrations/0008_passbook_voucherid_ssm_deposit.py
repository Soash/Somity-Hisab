# Generated by Django 5.1 on 2024-08-17 15:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otrans', '0007_passbook_category'),
        ('primary_setup', '0018_customuser_balance'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='passbook',
            name='VoucherID',
            field=models.CharField(blank=True, editable=False, max_length=50, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='SSM_Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processed_by', models.CharField(blank=True, max_length=50, null=True)),
                ('Date', models.DateField()),
                ('VoucherID', models.CharField(editable=False, max_length=50, unique=True)),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Note', models.CharField(blank=True, max_length=200, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primary_setup.branch')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
