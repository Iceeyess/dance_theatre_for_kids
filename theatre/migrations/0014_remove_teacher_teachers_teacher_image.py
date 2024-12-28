# Generated by Django 5.1.4 on 2024-12-28 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0013_regularclassschedule_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='image',
        ),
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, help_text='введите фото педагога', null=True, upload_to='image/', verbose_name='фотография'),
        ),
    ]
