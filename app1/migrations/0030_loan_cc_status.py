# Generated by Django 5.1 on 2024-08-20 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0029_remove_loanac_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan_cc',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('paid', 'Paid')], default='active', max_length=100),
        ),
    ]
