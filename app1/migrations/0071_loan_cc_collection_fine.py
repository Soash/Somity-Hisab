# Generated by Django 5.1 on 2024-08-31 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0070_customer_processed_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan_cc_collection',
            name='Fine',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
