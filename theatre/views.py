from django.shortcuts import render
import random
from django.views.generic import ListView, DetailView

from config.settings import topics, active_topics
from theatre.models import RegularClassSchedule, PlaybillSchedule, Teacher, Gallery
from users.models import BankAccountOrganization


# Create your views here.
def index(request):
    header_name = {'header_name': topics['main'],
                   'topics': topics,
                   'active_topics': active_topics}
    return render(request, 'index.html', context=header_name)

def schedule(request):
    event_1 = RegularClassSchedule.objects.all()
    event_2 = PlaybillSchedule.objects.all()
    result = list(event_1) + list(event_2)
    random.shuffle(result)
    data = dict(events=result, header_name=topics['schedule'], topics=topics, active_topics=active_topics)
    return render(request, 'schedule.html', context=data)

class TeacherListView(ListView):
    model = Teacher
    extra_context = {'header_name': topics['teachers'],
                     'topics': topics,
                     'active_topics': active_topics}
    template_name = 'teacher_list.html'


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher_detail.html'

class ContactsListView(ListView):
    model = BankAccountOrganization
    template_name = 'contact.html'
    extra_context = dict(header_name=topics['contacts'], topics=topics, active_topics=active_topics)

def news():
    ...

def about():
    ...

class GalleryListView(ListView):
    model = Gallery
    extra_context = dict(header_name=topics['gallery'], topics=topics, active_topics=active_topics)