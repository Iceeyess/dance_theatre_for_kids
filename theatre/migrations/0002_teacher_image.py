# Generated by Django 5.1.4 on 2024-12-24 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='image',
            field=models.ImageField(blank=True, help_text='введите фото педагога', null=True, upload_to='', verbose_name='фотография'),
        ),
    ]
