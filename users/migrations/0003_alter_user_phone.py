# Generated by Django 5.1.4 on 2024-12-24 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.PositiveIntegerField(help_text='Введите номер телефона', unique=True, verbose_name='телефонный номер'),
        ),
    ]
