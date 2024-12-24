from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """Функция создания 3х пользователей с разными вариациями полномочий для тестирования"""

    def handle(self, *args, **options):
        super_user = User.objects.create(
            username='admin',
            email='ice_eyes@mail.ru',
            is_superuser=True,
            is_staff=True,
            is_active=True,
            first_name='Дмитрий',
            last_name='Крашенинников',
            phone=9150483686
        )
        super_user.set_password('1234')
        super_user.save()
        user = User.objects.create(
            username='iceeyesss',
            email='iceeyesss@yandex.ru',
            is_superuser=False,
            is_staff=True,
            is_active=True,
            first_name='Дмитрий_2',
            last_name='Крашенинников_2',
            phone=9011234567
        )
        user.set_password('1234')
        user.save()
        low_user = User.objects.create(
            username='Павлик',
            email='pavlikkrolikov@yandex.ru',
            is_superuser=False,
            is_staff=False,
            is_active=True,
            first_name='Павлик',
            last_name='Кроликов',
            phone=9111234567
        )
        low_user.set_password('1234')
        low_user.save()