# Generated by Django 5.1 on 2024-08-22 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primary_setup', '0021_alter_dpsscheme_branch_alter_fdrscheme_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fdrscheme',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
