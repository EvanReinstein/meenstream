# Generated by Django 2.1.2 on 2018-10-29 20:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20181025_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(max_length=100, validators=[django.core.validators.EmailValidator()]),
        ),
    ]
