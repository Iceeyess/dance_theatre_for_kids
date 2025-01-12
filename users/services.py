import os

from django.core.mail import send_mail


def send_registration_email(form, link) -> None:
    subject = 'Поздравляем с регистрацией на сайте школы танцев Вероники Меркуловой.'
    body = f'''Добрый день, {form.get('first_name')}.
    
    Вы были зарегистрированы на сайте школы танцев Вероники Меркуловой.
    Ваши учетные записи:
    - Ваша электронная почта: {form.get('email')}.
    - Ваш телефон: {form.get('phone')}.
    - Ваш пароль: {form.get('password1')}.
    - Ваше имя: {form.get('first_name')}
    - Ваша фамилия: {form.get('last_name')}
    Для завершения регистрации перейдите по ссылке ниже.
    {link}
    
    Спасибо за регистрацию!
    с уважением,
    Администрация сайта школы танцев Вероники Меркуловой'''

    email_sender = os.getenv('EMAIL_HOST_USER')
    email_receiver = form.get('email')
    send_mail(subject=subject, message=body, from_email=email_sender, recipient_list=[email_receiver])