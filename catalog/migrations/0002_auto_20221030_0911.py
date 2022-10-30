# Generated by Django 3.2.16 on 2022-10-30 09:11

import Core.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='weight',
            field=models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(32766)]),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(validators=[Core.validators.validate_must_be_param]),
        ),
    ]
