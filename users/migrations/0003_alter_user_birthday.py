# Generated by Django 3.2.16 on 2022-11-27 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20221127_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='День рождения'),
        ),
    ]
