# Generated by Django 5.1 on 2024-08-26 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('otrans', '0013_salary_branch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary',
            name='month',
        ),
    ]