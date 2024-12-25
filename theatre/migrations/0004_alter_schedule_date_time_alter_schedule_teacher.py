# Generated by Django 5.1.4 on 2024-12-25 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0003_alter_teacher_options_alter_teacher_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='date_time',
            field=models.DateTimeField(help_text='Введите дату и время мероприятия', verbose_name='дата и время мероприятия'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='teacher',
            field=models.ManyToManyField(related_name='teacher', to='theatre.teacher', verbose_name='педагог'),
        ),
    ]