# Generated by Django 5.1.4 on 2024-12-24 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theatre', '0002_teacher_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ('last_name', 'first_name', 'middle_name'), 'verbose_name': 'педагог', 'verbose_name_plural': 'педагоги'},
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teachers',
            field=models.ImageField(blank=True, help_text='введите фото педагога', null=True, upload_to='teachers/', verbose_name='фотография'),
        ),
    ]
