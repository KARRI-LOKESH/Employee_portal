# Generated by Django 5.2.1 on 2025-05-26 07:01

import django.core.validators
import employees.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(default=employees.models.generate_employee_id, max_length=10, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('login_id', models.CharField(blank=True, max_length=50, unique=True)),
                ('date_of_birth', models.DateField()),
                ('department', models.CharField(choices=[('Engineering', 'Engineering'), ('Support', 'Support'), ('HR', 'HR'), ('Finance', 'Finance')], max_length=20)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('permanent_address', models.TextField()),
                ('current_address', models.TextField()),
                ('id_proof', models.FileField(upload_to='id_proofs/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
            ],
        ),
    ]
