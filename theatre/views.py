from django.shortcuts import render
import random
from theatre.models import RegularClassSchedule, PlaybillSchedule

topics = {
    'schedule': 'Расписание мероприятий',
    'price': 'Цены',
    'contacts': 'Контакты',
    'news': 'Новости',
    'about': 'О нас'
}

# Create your views here.
def index(request):
    return render(request, 'index.html')

def schedule(request):
    event_1 = RegularClassSchedule.objects.all()
    event_2 = PlaybillSchedule.objects.all()
    result = list(event_1) + list(event_2)
    random.shuffle(result)
    data = dict(events=result, header_name=topics['schedule'])
    return render(request, 'schedule.html', context=data)