from django.contrib import admin

from theatre.models import Teacher, Event, Address, Weekdays, RegularClassSchedule, PlaybillSchedule
from django.utils.html import format_html

# Register your models here.


admin.AdminSite.site_header = "Театр танцев Вероники Меркуловой."
admin.AdminSite.index_title = "Администрирование."


@admin.register(Weekdays)
class AdminWeekdays(admin.ModelAdmin):
    list_display = ('day', )
    list_display_links = ('day', )
    list_filter = ('day', )
    ordering = ('pk', )


@admin.register(Teacher)
class AdminTeacher(admin.ModelAdmin):

    def image_tag(self, obj):
        """Создаем вид мини-картинки в админке под каждого преподавателя"""
        return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>'.format(obj.image.url))

    image_tag.short_description = 'Фото'
    list_display = ('pk', 'last_name', 'first_name', 'middle_name', 'image_tag')
    list_display_links = ('pk', 'last_name', 'first_name', 'middle_name', 'image_tag',)
    list_filter = ('last_name',)
    search_fields = ('last_name', 'first_name', 'middle_name')
    ordering = ('pk',)
    empty_value_display = '-'


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk', 'name',)
    list_filter = ('name',)
    search_fields = ('pk', 'name',)
    ordering = ('pk',)
    empty_value_display = '-'


@admin.register(Address)
class AdminAddress(admin.ModelAdmin):
    list_display = ('pk', 'country', 'post_code', 'district', 'city', 'street', 'house', 'apartment',)
    list_display_links = ('pk', 'country', 'post_code', 'district', 'city', 'street', 'house', 'apartment',)
    list_filter = ('city', 'street',)
    search_fields = ('city', 'street',)
    ordering = ('pk',)
    empty_value_display = '-'


@admin.register(RegularClassSchedule)
class RegularClassScheduleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'event', 'days_list', 'time', 'full_name', )
    list_display_links = ('pk', 'event', 'days_list', 'time', 'full_name', )
    list_filter = ('event', 'time', 'teacher', )
    search_fields = ('event', 'teacher', 'address', )
    ordering = ('pk', )
    empty_value_display = '-'

    @admin.display(description='ФИО преподавателей')
    def full_name(self, schedule: RegularClassSchedule):
        """Функция отображения ФИО преподавателя в отедльной колонке"""
        result = list(map(lambda a:
                                 f'{a.last_name} {a.first_name[0]}.{a.middle_name[0]}.'
                                 if a.middle_name
                                 else f'{a.last_name} {a.first_name[0]}.',
                                 schedule.teacher.all()))
        return result

    @admin.display(description='Дни недели')
    def days_list(self, schedule: RegularClassSchedule):
        """Функция отображения дней недели в отдельной колонке"""
        result = ', '.join(map(lambda a: a.day, schedule.weekdays.all()))
        return result

@admin.register(PlaybillSchedule)
class PlaybillScheduleAdmin(RegularClassScheduleAdmin):
    """Переопределенный класс для больших мероприятий"""
    list_display = ('pk', 'event', 'date_time', 'full_name', )
    list_display_links = ('pk', 'event', 'date_time', 'full_name', )
    list_filter = ('event', 'date_time',  'teacher', )



