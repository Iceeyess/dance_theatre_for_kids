from theatre.apps import TheatreConfig
from django.urls import path
from .views import index, schedule, TeacherListView, TeacherDetailView, news, about, ContactsListView, GalleryListView, \
    GalleryCreateView, get_mark_deletion, deletion_form, get_deletion, get_restore, GalleryDetailView, \
    get_streaming_video

app_name = TheatreConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('schedule/', schedule, name='schedule'),
    path('teachers/', TeacherListView.as_view(), name='teachers'),
    path('teachers/<int:pk>', TeacherDetailView.as_view(), name='teachers_detail'),
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    path('news/', news, name='news'),
    path('about/', about, name='about'),
    #  Галерея:
    path('gallery/', GalleryListView.as_view(), name='gallery'),  # Галерея состоит из смешанных фото и видео файлов
    path('gallery/creation/', GalleryCreateView.as_view(), name='gallery-creation'),  # Форма создания фото/видео
    path('gallery/deletion/', deletion_form, name='gallery-deletion-form'),  # Форма восстановления/удаления фото
    path('gallery/deletion/<int:pk>', get_deletion, name='gallery-deletion'),  # Триггер на удаление фото/видео
    path('gallery/restore/<int:pk>', get_restore, name='gallery-restore'),  # Триггер на восстановление фото/видео
    path('gallery/deletion_mark/<int:pk>', get_mark_deletion, name='gallery-deletion-mark'),  # Пометка на удаление фото/видео
    path('gallery/detail/<int:pk>', GalleryDetailView.as_view(), name='gallery-detail'),  # Детализация фото/видео
    path('gallery/detail/stream/<int:pk>', get_streaming_video, name='gallery-stream'),  # для потокового видео
    #
]
