from django.contrib.auth.views import LogoutView

from users.apps import UsersConfig
from django.urls import path

from users.views import UserRegistration, UserLoginView, email_verification, ProfileView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('registration-email-confirm/<str:token>/', email_verification, name='email-confirm'),

]
