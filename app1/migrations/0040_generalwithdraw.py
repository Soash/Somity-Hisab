# Generated by Django 5.1 on 2024-08-21 16:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0039_generaldeposit'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralWithdraw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Note', models.CharField(blank=True, max_length=200, null=True)),
                ('VoucherID', models.CharField(blank=True, editable=False, max_length=50, null=True, unique=True)),
                ('processed_by', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('general', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='general_withdraw', to='app1.generalac')),
            ],
        ),
    ]
