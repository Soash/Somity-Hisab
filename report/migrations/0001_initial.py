# Generated by Django 5.1 on 2024-08-30 10:36

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0070_customer_processed_by_and_more'),
        ('primary_setup', '0026_alter_vouchercategory_category_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('debit', 'Debit'), ('credit', 'Credit')], max_length=6)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('description', models.CharField(default='', max_length=300)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primary_setup.branch')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.customer')),
                ('processed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
