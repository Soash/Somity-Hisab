# Generated by Django 5.1 on 2024-08-22 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0043_fdr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fdr',
            old_name='starte_date',
            new_name='start_date',
        ),
        migrations.AddField(
            model_name='fdr',
            name='note',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
