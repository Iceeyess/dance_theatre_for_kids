from django import template
from  os.path import join

from config.settings import MEDIA_URL, BASE_DIR

register = template.Library()

# Создание тега
@register.filter(name='get_url_picture')
def concatenate_paths(variable, static_path):
    print(BASE_DIR)
    if variable:
        return join(MEDIA_URL, str(variable))
    return join(BASE_DIR, str(static_path))