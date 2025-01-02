# Generated by Django 5.1.4 on 2025-01-01 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_bankaccountorganization_payment_purpose'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccountorganization',
            name='full_name',
        ),
        migrations.AlterField(
            model_name='bankaccountorganization',
            name='tin_number',
            field=models.PositiveBigIntegerField(verbose_name='ИНН'),
        ),
    ]