from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from  django import forms
# Create your models here.


NULLABLE = dict(null=True, blank=True)


class AddressOrganization(models.Model):
    """Класс адреса"""
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица', **NULLABLE)
    house = models.CharField(max_length=100, verbose_name='дом', **NULLABLE)
    apartment = models.CharField(max_length=100, verbose_name='квартира', **NULLABLE)

    class Meta:
        verbose_name = 'адрес организации'
        verbose_name_plural = 'адреса организации'
        ordering = ('pk', )

    def __str__(self):
        return f'{self.country} {self.city} {self.street} {self.house} {self.apartment}'

class BankAccountOrganization(models.Model):
    """Класс банковских счетов нашей организации"""
    account_number = models.CharField(max_length=20, verbose_name='расчетный счет')
    bic_code = models.PositiveIntegerField(verbose_name='БИК банка')
    tin_number = models.PositiveBigIntegerField(verbose_name='ИНН')
    organization = models.ForeignKey('Organization', on_delete=models.SET_NULL, **NULLABLE)

    class Meta:
        verbose_name = 'банковские реквизиты организации'
        verbose_name_plural = 'банковские реквизиты организации'
        ordering = ('pk', )

    def __str__(self):
        return f'{self.organization}, {self.tin_number}'

    def clean(self):
        if [True for _ in str(self.account_number) if not _.isdigit()]:
            raise forms.ValidationError('Номер банковского счета должен содержать только цифры в формате \'40702812345678901234\'.')
        if len(str(self.account_number)) < 20:
            raise forms.ValidationError('Номер банковского счета должен состоять из 20 цифр.')
        return super().clean()


class Organization(models.Model):
    """Класс с информацией для нашей организации"""
    org_name = models.CharField(max_length=150, verbose_name='организация')
    phone = models.CharField(max_length=10)
    address = models.ForeignKey(AddressOrganization, on_delete=models.DO_NOTHING, verbose_name='адрес')

    def clean(self):
        """Валидатор телефона"""
        if [True for _ in self.phone if not _.isdigit()]:
            raise forms.ValidationError('Телефон должен содержать только цифры в формате \'9011234567\'.')
        if len(self.phone)!= 10:
            raise forms.ValidationError('Телефон должен состоять из 10 цифр.')
        return super().clean()

    class Meta:
        verbose_name = 'организация'
        verbose_name_plural = 'организации'
        ordering = ('pk', )

    def __str__(self):
        return self.org_name


class User(AbstractUser):
    """Класс пользователей"""
    email = models.EmailField(unique=True, verbose_name='электронная почта', help_text='Введите электронную почту')
    username = models.CharField(unique=True, max_length=150, verbose_name='имя пользователя',
                                help_text='Введите имя пользователя')
    avatar = models.ImageField(verbose_name='фотография', help_text='вложите файл с фотографией',
                               upload_to='users/', **NULLABLE)
    phone = models.CharField(max_length=10, unique=True, verbose_name='телефонный номер',
                                        help_text='Введите номер телефона')
    is_active = models.BooleanField(default=False, verbose_name='статус пользователя',
                                    help_text='Пользователь активен?')
    #  Переопределили поле для входа
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return f'Email: {self.email}, Username: {self.username}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('pk', )

    def clean(self):
        """Валидатор телефона"""
        if [True for _ in self.phone if not _.isdigit()]:
            raise forms.ValidationError('Телефон должен содержать только цифры в формате \'9011234567\'.')
        if len(self.phone)!= 10:
            raise forms.ValidationError('Телефон должен состоять из 10 цифр.')
        return super().clean()