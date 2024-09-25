# Generated by Django 5.1 on 2024-08-20 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0026_loan_special_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanac',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('paid', 'Paid')], default='active', max_length=100),
        ),
        migrations.AlterField(
            model_name='loan_special_collection',
            name='Amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Paid Intererst'),
        ),
    ]
