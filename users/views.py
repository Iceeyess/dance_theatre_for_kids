import secrets

from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from users.forms import UserRegistrationForm, UserLoginForm
from users.models import User
from config.settings import topics, active_topics
from users.services import send_registration_email


# Create your views here.
class UserRegistration(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.token = secrets.token_hex(16)
        host = self.request.get_host()
        user.save()
        url = f'http://{host}/users/registration-email-confirm/{user.token}/'
        send_registration_email(form.cleaned_data, url)
        return super().form_valid(form)



class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    extra_context = {'header_name': topics['login'],
                     'active_topics': active_topics}

def user_logout(request):
    logout(request)
    return redirect(reverse('theatre:index'))


def email_verification(request, token):
    """Функция для активации пользователя"""
    user = get_object_or_404(User, token=token)
    if user:
        user.is_active = True
        user.save()
        return redirect(reverse('users:login'))

class ProfileView(DetailView):
    model = User
