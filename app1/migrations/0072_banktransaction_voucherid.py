# Generated by Django 5.1 on 2024-08-31 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0071_loan_cc_collection_fine'),
    ]

    operations = [
        migrations.AddField(
            model_name='banktransaction',
            name='VoucherID',
            field=models.CharField(blank=True, editable=False, max_length=50, null=True, unique=True),
        ),
    ]