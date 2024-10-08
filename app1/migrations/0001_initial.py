# Generated by Django 5.1 on 2024-08-15 13:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('primary_setup', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='primary_setup.branch')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_type', models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('half_monthly', 'Half Monthly'), ('monthly', 'Monthly'), ('half_yearly', 'Half Yearly'), ('yearly', 'Yearly')], max_length=20)),
                ('joining_date', models.DateField()),
                ('account_no', models.CharField(max_length=20, unique=True)),
                ('admission_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('admission_form_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pass_book', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('special_savings_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('password', models.CharField(max_length=100)),
                ('general_savings_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('add_share_ac', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3)),
                ('previous_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('nominee', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15)),
                ('spouse_name', models.CharField(blank=True, max_length=100, null=True)),
                ('national_id_number', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('religion', models.CharField(choices=[('islam', 'Islam'), ('hinduism', 'Hinduism'), ('buddhism', 'Buddhism'), ('christianity', 'Christianity'), ('other', 'Other')], default='Islam', max_length=50)),
                ('customer_father', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_mother', models.CharField(blank=True, max_length=100, null=True)),
                ('secondary_number', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('profession', models.CharField(blank=True, max_length=100, null=True)),
                ('business_name', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_birth', models.DateField()),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('signature_card', models.ImageField(blank=True, null=True, upload_to='signature_cards/')),
                ('national_id_copy', models.ImageField(blank=True, null=True, upload_to='national_id_copies/')),
                ('current_village', models.CharField(blank=True, max_length=100, null=True)),
                ('current_post_office', models.CharField(blank=True, max_length=100, null=True)),
                ('current_thana', models.CharField(blank=True, max_length=100, null=True)),
                ('current_district', models.CharField(blank=True, max_length=100, null=True)),
                ('permanent_village', models.CharField(blank=True, max_length=100, null=True)),
                ('permanent_post_office', models.CharField(blank=True, max_length=100, null=True)),
                ('permanent_thana', models.CharField(blank=True, max_length=100, null=True)),
                ('permanent_district', models.CharField(blank=True, max_length=100, null=True)),
                ('nominee_name', models.CharField(blank=True, max_length=100, null=True)),
                ('nominee_relation', models.CharField(blank=True, max_length=100, null=True)),
                ('nominee_father', models.CharField(blank=True, max_length=100, null=True)),
                ('nominee_mother', models.CharField(blank=True, max_length=100, null=True)),
                ('nominee_national_id', models.CharField(blank=True, max_length=20, null=True)),
                ('nominee_mobile_number', models.CharField(blank=True, max_length=15, null=True)),
                ('nominee_address', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=10)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primary_setup.branch')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primary_setup.somity')),
            ],
        ),
        migrations.CreateModel(
            name='LoanAC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('loan_scheme', models.CharField(max_length=100)),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('profit_percent', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('profit_taka', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('number_of_installments', models.IntegerField()),
                ('installment_sequence', models.CharField(blank=True, max_length=100, null=True)),
                ('installment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_installment', models.IntegerField(default=0)),
                ('fine_per_missed_installment', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('loan_category', models.CharField(max_length=100)),
                ('insurance_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('loan_form_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('share', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('stamp_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('risk_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('other_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('stamp_information', models.TextField(blank=True, null=True)),
                ('bank_and_cheque_information', models.TextField(blank=True, null=True)),
                ('transaction_id', models.CharField(editable=False, max_length=15, unique=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.customer')),
            ],
        ),
    ]
