# Generated by Django 3.2.16 on 2022-11-20 08:25

from django.db import migrations, models

import Core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20221120_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(help_text='Введите описание товара', validators=[Core.validators.validate_must_be_param], verbose_name='Описание'),
        ),
    ]