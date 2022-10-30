# Generated by Django 3.2.16 on 2022-10-30 10:16

import Core.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20221030_0911'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категорию', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.AlterField(
            model_name='category',
            name='is_published',
            field=models.BooleanField(default=True, help_text='Это поле отвечает за публикацию', verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Это поле отвечает за название', max_length=150, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text='Это идентификатор', max_length=200, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')], verbose_name='Идентификатор'),
        ),
        migrations.AlterField(
            model_name='category',
            name='weight',
            field=models.IntegerField(default=100, help_text='Это поле отвечает за вес товара', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(32766)], verbose_name='Вес'),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(help_text='Это поле отвечает за категорию товара', on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='item',
            name='is_published',
            field=models.BooleanField(default=True, help_text='Это поле отвечает за публикацию', verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(help_text='Это поле отвечает за название', max_length=150, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(help_text='Это поле отвечает за теги товара, их может быть очень много', related_name='tag', to='catalog.Tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(help_text='Это поле отвечает за описание товара', validators=[Core.validators.validate_must_be_param], verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='is_published',
            field=models.BooleanField(default=True, help_text='Это поле отвечает за публикацию', verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(help_text='Это поле отвечает за название', max_length=150, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(help_text='Это идентификатор', max_length=200, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')], verbose_name='Идентификатор'),
        ),
    ]