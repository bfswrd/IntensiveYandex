# Generated by Django 3.2.16 on 2022-11-27 17:29

from django.db import migrations, models

import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('object', users.models.CustomUserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='Введите почту', max_length=254, unique=True, verbose_name='Email address'),
        ),
    ]