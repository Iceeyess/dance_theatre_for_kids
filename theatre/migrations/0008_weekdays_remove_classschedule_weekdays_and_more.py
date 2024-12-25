# Generated by Django 5.1.4 on 2024-12-25 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0007_remove_classschedule_weekdays_delete_weekdays_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weekdays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(help_text='Введите день недели', max_length=30, verbose_name='день недели')),
            ],
        ),
        migrations.RemoveField(
            model_name='classschedule',
            name='weekdays',
        ),
        migrations.AddField(
            model_name='classschedule',
            name='weekdays',
            field=models.ManyToManyField(help_text='Выберите дни недели', to='theatre.weekdays', verbose_name='день недели'),
        ),
    ]
