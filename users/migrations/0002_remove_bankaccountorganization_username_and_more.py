# Generated by Django 5.1.4 on 2025-01-01 20:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccountorganization',
            name='username',
        ),
        migrations.AddField(
            model_name='bankaccountorganization',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.organization'),
        ),
    ]
