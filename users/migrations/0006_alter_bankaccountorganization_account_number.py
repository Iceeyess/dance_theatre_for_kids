# Generated by Django 5.1.4 on 2025-01-01 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_bankaccountorganization_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccountorganization',
            name='account_number',
            field=models.CharField(max_length=20, verbose_name='расчетный счет'),
        ),
    ]
