# Generated by Django 5.1.4 on 2024-12-25 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0008_weekdays_remove_classschedule_weekdays_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weekdays',
            options={'verbose_name': 'день недели', 'verbose_name_plural': 'дни недели'},
        ),
    ]
