# Generated by Django 5.1 on 2024-08-15 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('primary_setup', '0002_customuser_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='group',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group'),
        ),
    ]