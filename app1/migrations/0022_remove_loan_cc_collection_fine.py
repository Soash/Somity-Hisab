# Generated by Django 5.1 on 2024-08-20 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_loan_cc_loan_cc_collection_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan_cc_collection',
            name='Fine',
        ),
    ]
