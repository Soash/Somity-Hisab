# Generated by Django 5.1 on 2024-08-21 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0037_alter_generalac_branch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalac',
            name='branch',
        ),
    ]