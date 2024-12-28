from theatre.apps import TheatreConfig
from django.urls import path
from .views import index, schedule, TeacherListView, TeacherDetailView, contacts, news, about

app_name = TheatreConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('schedule/', schedule, name='schedule'),
    path('teachers/', TeacherListView.as_view(), name='teachers'),
    path('teachers/<int:pk>', TeacherDetailView.as_view(), name='teachers_detail'),
    path('contacts/', contacts, name='contacts'),
    path('news/', news, name='news'),
    path('about/', about, name='about'),
]
