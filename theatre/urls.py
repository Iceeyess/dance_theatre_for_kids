from theatre.apps import TheatreConfig
from django.urls import path
from .views import index, schedule

app_name = TheatreConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('schedule/', schedule, name='schedule'),
]
