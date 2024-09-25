# Generated by Django 5.1 on 2024-08-22 02:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0041_generaltransactionhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavingsAC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regular_target', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_deposit', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('total_withdraw', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Close', 'Close')], default='Active', max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.customer')),
            ],
        ),
        migrations.CreateModel(
            name='SavingsDeposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Note', models.CharField(blank=True, max_length=200, null=True)),
                ('VoucherID', models.CharField(blank=True, editable=False, max_length=50, null=True, unique=True)),
                ('processed_by', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('general', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='savings_general_deposit', to='app1.savingsac')),
            ],
        ),
        migrations.CreateModel(
            name='SavingsTransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('deposit', 'Deposit'), ('withdraw', 'Withdraw')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('processed_by', models.CharField(blank=True, max_length=200, null=True)),
                ('note', models.CharField(blank=True, max_length=200, null=True)),
                ('current_balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('general', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='savings_transaction_history', to='app1.savingsac')),
            ],
        ),
        migrations.CreateModel(
            name='SavingsWithdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Note', models.CharField(blank=True, max_length=200, null=True)),
                ('VoucherID', models.CharField(blank=True, editable=False, max_length=50, null=True, unique=True)),
                ('processed_by', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('general', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='savings_general_withdraw', to='app1.savingsac')),
            ],
        ),
    ]