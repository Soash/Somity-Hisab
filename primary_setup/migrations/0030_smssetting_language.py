# Generated by Django 5.1 on 2024-09-01 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primary_setup', '0029_remove_smssetting_content_english_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='smssetting',
            name='language',
            field=models.CharField(choices=[('bangla', 'Bangla'), ('english', 'English')], default='bangla', max_length=20),
        ),
    ]
