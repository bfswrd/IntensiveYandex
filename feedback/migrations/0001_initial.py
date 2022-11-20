# Generated by Django 3.2.16 on 2022-11-20 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Введите обращение', verbose_name='Обратная связь')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
        ),
    ]
