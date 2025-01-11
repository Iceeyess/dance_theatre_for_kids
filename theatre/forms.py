from django import forms
from .models import Gallery, PlaybillSchedule


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class PhotoForm(forms.Form):
    """Форма для загрузки фоток"""
    event = forms.ModelChoiceField(queryset=PlaybillSchedule.objects.all(), widget=forms.Select, label='Мероприятие')
    image = MultipleFileField(label='Фотографии', required=True, help_text='Выберите фотографии для загрузки')

