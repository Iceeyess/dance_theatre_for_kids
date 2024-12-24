from theatre.apps import TheatreConfig
from django.urls import path
from .views import index


app_name = TheatreConfig.name

urlpatterns = [
    path('', index)
]
