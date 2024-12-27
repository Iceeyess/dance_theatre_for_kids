from django import template
from  os.path import join

from config.settings import MEDIA_URL

register = template.Library()


@register.simple_tag
def get_url_picture(data):
    return join(MEDIA_URL, str(data))



# Создание тега
# @register.filter(name='get_url_picture')
# def concatenate_paths(variable, static_path):
#     if variable:
#         return join(MEDIA_URL, str(variable))
#     return join(BASE_DIR, str(static_path))