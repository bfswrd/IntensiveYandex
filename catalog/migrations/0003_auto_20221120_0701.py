# Generated by Django 3.2.16 on 2022-11-20 07:01

import Core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20221113_0957'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('name',), 'verbose_name': 'товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(help_text='Введите описание товара', validators=[Core.validators.validate_must_be_param], verbose_name='Описание'),
        ),
    ]
