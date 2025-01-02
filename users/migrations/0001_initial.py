# Generated by Django 5.1.4 on 2025-01-01 19:20

import django.contrib.auth.models
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100, verbose_name='страна')),
                ('city', models.CharField(max_length=100, verbose_name='город')),
                ('street', models.CharField(blank=True, max_length=100, null=True, verbose_name='улица')),
                ('house', models.CharField(blank=True, max_length=100, null=True, verbose_name='дом')),
                ('apartment', models.CharField(blank=True, max_length=100, null=True, verbose_name='квартира')),
            ],
            options={
                'verbose_name': 'адрес организации',
                'verbose_name_plural': 'адреса организации',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(help_text='Введите электронную почту', max_length=254, unique=True, verbose_name='электронная почта')),
                ('username', models.CharField(help_text='Введите имя пользователя', max_length=150, unique=True, verbose_name='имя пользователя')),
                ('avatar', models.ImageField(blank=True, help_text='вложите файл с фотографией', null=True, upload_to='users/', verbose_name='фотография')),
                ('phone', models.CharField(help_text='Введите номер телефона', max_length=10, unique=True, verbose_name='телефонный номер')),
                ('is_active', models.BooleanField(default=False, help_text='Пользователь активен?', verbose_name='статус пользователя')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
                'ordering': ('pk',),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BankAccountOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10000000000000000000), django.core.validators.MaxValueValidator(99999999999999999999)], verbose_name='расчетный счет')),
                ('bic_code', models.PositiveIntegerField(verbose_name='БИК банка')),
                ('tin_number', models.PositiveIntegerField(verbose_name='ИНН')),
                ('full_name', models.CharField(max_length=250, verbose_name='ИП ФИО/наименование организации')),
                ('payment_purpose', models.CharField(blank=True, max_length=208, null=True, verbose_name='назначение платежа')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'банковские реквизиты организации',
                'verbose_name_plural': 'банковские реквизиты организации',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=150, verbose_name='организация')),
                ('phone', models.CharField(max_length=10)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.addressorganization', verbose_name='адрес')),
            ],
            options={
                'verbose_name': 'организация',
                'verbose_name_plural': 'организации',
                'ordering': ('pk',),
            },
        ),
    ]
