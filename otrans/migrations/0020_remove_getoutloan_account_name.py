# Generated by Django 5.1 on 2024-08-27 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('otrans', '0019_getoutloan_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='getoutloan',
            name='account_name',
        ),
    ]