from django.db import models
from django.db.models import DO_NOTHING

# Create your models here.


NULLABLE = dict(null=True, blank=True)


class Teacher(models.Model):
    """Класс-описания модели педагогов"""
    first_name = models.CharField(max_length=100, verbose_name='имя', help_text='Введите имя педагога')
    last_name = models.CharField(max_length=100, verbose_name='фамилия', help_text='Введите фамилию педагога')
    middle_name = models.CharField(max_length=100, verbose_name='отчество',
                                   help_text='Введите отчество педагога', **NULLABLE)
    birthday = models.DateField(verbose_name='дата рождения', help_text='Введите дату рождения')
    specialty = models.CharField(max_length=150, verbose_name='специальность',
                                 help_text='Введите специальность', **NULLABLE)
    biography = models.TextField(verbose_name='биография', help_text='Введите биографию', **NULLABLE)
    image = models.ImageField(upload_to='teachers/', verbose_name='фотография', help_text='введите фото педагога',
                              **NULLABLE)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    @property
    def get_full_name(self):
        """Функция отображения ФИО преподавателя в отдельной колонке"""
        return f'{self.last_name} {self.first_name} {self.middle_name}' if self.middle_name \
            else f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'педагог'
        verbose_name_plural = 'педагоги'
        ordering = ('last_name', 'first_name', 'middle_name')


class Event(models.Model):
    """Класс-описания модели мероприятия"""
    name = models.CharField(max_length=150, verbose_name='наименование мероприятия',
                            help_text='Введите название мероприятия')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'мероприятие'
        verbose_name_plural = 'мероприятия'


class Address(models.Model):
    """Класс-описания модели адреса"""
    country = models.CharField(max_length=100, verbose_name='страна', help_text='Введите страну')
    post_code = models.CharField(max_length=6, verbose_name='почтовый индекс',
                                 help_text='Введите почтовый индекс', **NULLABLE)
    district = models.CharField(max_length=150, verbose_name='область', help_text='Введите область', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', help_text='Введите город', **NULLABLE)
    street = models.CharField(max_length=150, verbose_name='улица', help_text='Введите улицу', **NULLABLE)
    house = models.CharField(max_length=20, verbose_name='дом', help_text='Введите дом', **NULLABLE)
    apartment = models.CharField(max_length=20, verbose_name='квартира', help_text='Введите квартиру', **NULLABLE)

    def __str__(self):
        address_list = [
            self.post_code, self.country, self.city, self.district, self.street, self.house, self.apartment

        ]
        return ', '.join([_ for _ in address_list if _])

    class Meta:
        verbose_name = 'адрес'
        verbose_name_plural = 'адреса'


class Weekdays(models.Model):
    """Класс определения названий дней недели"""
    day = models.CharField(max_length=30, verbose_name='день недели', help_text='Введите день недели')

    def __str__(self):
        return self.day

    class Meta:
        verbose_name = 'день недели'
        verbose_name_plural = 'дни недели'


class RegularClassSchedule(models.Model):
    """Класс-описания модели расписания регулярных занятий с периодически-повторяющимся циклом"""
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING, verbose_name='наименование мероприятия')
    weekdays = models.ManyToManyField(Weekdays, verbose_name='день недели', help_text='Выберите дни недели')
    time = models.TimeField(verbose_name='время занятий',
                            help_text='Введите время занятий')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='дата и время обновления')
    teacher = models.ManyToManyField(Teacher, verbose_name='педагог', related_name='teacher_regular_event')
    address = models.ForeignKey(Address, on_delete=DO_NOTHING, verbose_name='адрес мероприятия')
    picture = models.ImageField(upload_to='regular_event_pict/', verbose_name='Фотка мероприятия', **NULLABLE)
    price = models.FloatField(default=0, verbose_name='Стоимость', help_text='Введите стоимость услуги')

    def __str__(self):
        return f'{self.event.name} - {self.time}'

    @property
    def weekday_names(self):
        return ', '.join([weekday.day for weekday in self.weekdays.all()])

    @property
    def teacher_names(self):
        result = ', '.join(list(map(lambda a:
                                    f'{a.last_name} {a.first_name[0]}.{a.middle_name[0]}.'
                                    if a.middle_name
                                    else f'{a.last_name} {a.first_name[0]}.',
                                    self.teacher.all())))
        return result

    class Meta:
        verbose_name = 'расписание регулярного занятия'
        verbose_name_plural = 'расписание регулярных занятий'


class PlaybillSchedule(models.Model):
    """Класс-описания модели расписания Грандиозных выступлений на сцене"""
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING, verbose_name='наименование мероприятия')
    date_time = models.DateTimeField(verbose_name='дата и время мероприятия',
                                     help_text='Введите дату и время мероприятия')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='дата и время обновления')
    teacher = models.ManyToManyField(Teacher, verbose_name='педагог', related_name='teacher_big_event')
    address = models.ForeignKey(Address, on_delete=DO_NOTHING, verbose_name='адрес мероприятия')
    picture = models.ImageField(upload_to='playbill_event_pict/', verbose_name='Фотка мероприятия', **NULLABLE)

    def __str__(self):
        return f'{self.event.name} - {self.date_time}'

    @property
    def teacher_names(self):
        result = ', '.join(list(map(lambda a:
                                    f'{a.last_name} {a.first_name[0]}.{a.middle_name[0]}.'
                                    if a.middle_name
                                    else f'{a.last_name} {a.first_name[0]}.',
                                    self.teacher.all())))
        return result

    class Meta:
        verbose_name = 'расписание большого мероприятия'
        verbose_name_plural = 'расписание больших мероприятий'
