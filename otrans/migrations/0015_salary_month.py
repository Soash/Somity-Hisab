# Generated by Django 5.1 on 2024-08-26 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otrans', '0014_remove_salary_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='month',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]