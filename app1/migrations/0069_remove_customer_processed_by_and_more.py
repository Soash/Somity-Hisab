# Generated by Django 5.1 on 2024-08-30 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0068_loancollection_processed_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='processed_by',
        ),
        migrations.RemoveField(
            model_name='dpstransactionhistory',
            name='processed_by',
        ),
        migrations.RemoveField(
            model_name='dpswithdraw',
            name='processed_by',
        ),
        migrations.RemoveField(
            model_name='fdr',
            name='processed_by',
        ),
        migrations.RemoveField(
            model_name='fdrtransactionhistory',
            name='processed_by',
        ),
        migrations.RemoveField(
            model_name='generaldeposit',
            name='processed_by',
        ),
        migrations.RemoveField(
            model_name='generaltransactionhistory',
            name='processed_by',
        ),
        migrations.RemoveField(
            model_name='generalwithdraw',
            name='processed_by',
        ),
        migrations.RemoveField(
            model_name='loan_cc_collection',
            name='processed_by',
        ),
        migrations.RemoveField(
            model_name='loan_special',
            name='processed_by',
        ),
        migrations.RemoveField(
            model_name='loan_special_collection',
            name='processed_by',
        ),
        migrations.RemoveField(
            model_name='savingsdeposit',
            name='processed_by',
        ),
        migrations.RemoveField(
            model_name='savingstransactionhistory',
            name='processed_by',
        ),
        migrations.RemoveField(
            model_name='savingswithdraw',
            name='processed_by',
        ),
        migrations.RemoveField(
            model_name='shareactransactionhistory',
            name='processed_by',
        ),
    ]