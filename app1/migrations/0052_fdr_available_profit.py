# Generated by Django 5.1 on 2024-08-22 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0051_remove_fdr_available_profit_remove_fdr_total_profit'),
    ]

    operations = [
        migrations.AddField(
            model_name='fdr',
            name='available_profit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]