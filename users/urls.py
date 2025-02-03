from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

from users.apps import UsersConfig
from django.urls import path, reverse_lazy

from users.views import UserRegistration, UserLoginView, email_verification, ProfileView, user_logout, \
    UserPasswordResetConfirm

app_name = UsersConfig.name

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistration.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', user_logout, name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('registration-email-confirm/<str:token>/', email_verification, name='email-confirm'),
    # Восстановление пароля
    path('password-reset', PasswordResetView.as_view(template_name='users/reset/password_reset_form.html',
                                                     email_template_name='users/reset/password_reset_email.html',
                                                     success_url=reverse_lazy('users:password-reset-done')),
         name='password-reset'),
    path('password-reset/done', PasswordResetDoneView.as_view(template_name='users/reset/password_reset_done.html'),
         name='password-reset-done'),
    path('password-reset/<uidb64>/<token>/',
         UserPasswordResetConfirm.as_view(),
         name='password-reset-confirm'),
    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name='users/reset/password_reset_complete.html'),
         name='password-reset-complete')

]
