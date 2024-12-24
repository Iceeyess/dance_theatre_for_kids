from django.contrib import admin

from theatre.models import Teacher, Event, Address, Schedule
from django.utils.html import format_html
# Register your models here.


admin.AdminSite.site_header = "Театр танцев Вероники Меркуловой."
admin.AdminSite.index_title = "Администрирование."


@admin.register(Teacher)
class AdminTeacher(admin.ModelAdmin):

    def image_tag(self, obj):
        """Создаем вид мини-картинки в админке под каждого преподавателя"""
        return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>'.format(obj.image.url))

    image_tag.short_description = 'Фото'
    list_display = ('pk', 'last_name', 'first_name', 'middle_name', 'image_tag')
    list_display_links = ('pk', 'last_name', 'first_name', 'image_tag', )
    list_filter = ('last_name', )
    search_fields = ('last_name', 'first_name', 'middle_name')
    ordering = ('pk', )
    empty_value_display = '-'


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    list_display = ('pk', 'name', )
    list_filter = ('name', )
    search_fields = ('pk', 'name', )
    ordering = ('pk', )
    empty_value_display = '-'


@admin.register(Address)
class AdminAddress(admin.ModelAdmin):
    list_display = ('pk', 'country', 'post_code', 'district', 'city', 'street', 'house', 'apartment', )
    list_display_links = ('pk', 'country', 'post_code', 'district', 'city', 'street', 'house', 'apartment', )
    list_filter = ('city', 'street', )
    search_fields = ('city', 'street',)
    ordering = ('pk', )
    empty_value_display = '-'


@admin.register(Schedule)
class ScheduleAddress(admin.ModelAdmin):
    list_display = ('pk', 'event', 'date_time', 'full_name', )
    list_display_links = ('pk', 'event', 'date_time', )
    list_filter = ('event', 'date_time', 'teacher', )
    search_fields = ('event', 'teacher', 'address')
    ordering = ('pk', )
    empty_value_display = '-'

    @admin.display(description='ФИО')
    def full_name(self, schedule: Schedule):
        ...
