# Generated by Django 5.1.4 on 2024-12-25 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0010_playbillschedule_regularclassschedule_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playbillschedule',
            options={'verbose_name': 'расписание большого мероприятия', 'verbose_name_plural': 'расписание больших мероприятий'},
        ),
    ]
