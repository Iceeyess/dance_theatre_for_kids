from django import template
from  os.path import join

from config.settings import MEDIA_URL, STATIC_ROOT, BASE_DIR

register = template.Library()


@register.simple_tag
def get_url_picture(data):
    print(BASE_DIR, )
    if data:
        return join(MEDIA_URL, str(data))
    return join(STATIC_ROOT, "photo/system/no_picture.jpg")


# Создание тега
# @register.filter(name='get_url_picture')
# def concatenate_paths(variable, arg):
#     static_path = 'static/photo/event_no_picture/no_picture.jpg'  # Путь к статической картинке по умолчанию
#     if variable:
#         return join(MEDIA_URL, str(variable))
#     return join(BASE_DIR, str(static_path))