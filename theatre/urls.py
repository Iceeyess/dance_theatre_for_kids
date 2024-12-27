from theatre.apps import TheatreConfig
from django.urls import path
from .views import index, schedule, TeacherListView, TeacherDetailView

app_name = TheatreConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('schedule/', schedule, name='schedule'),
    path('teachers/', TeacherListView.as_view(), name='teachers'),
    path('teachers/<int:pk>', TeacherDetailView.as_view(), name='teachers_detail'),
]
