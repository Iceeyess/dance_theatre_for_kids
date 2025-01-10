import os

from django.shortcuts import render, redirect
import random

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.views.generic.edit import FormView
from config.settings import topics, active_topics
from theatre.apps import TheatreConfig
from theatre.forms import PhotoForm

from theatre.models import RegularClassSchedule, PlaybillSchedule, Teacher, Gallery
from users.models import BankAccountOrganization


# Create your views here.
def index(request):
    header_name = {'header_name': topics['main'],
                   'topics': topics,
                   'active_topics': active_topics}
    return render(request, os.path.join(TheatreConfig.name,'index.html'), context=header_name)

def schedule(request):
    event_1 = RegularClassSchedule.objects.all()
    event_2 = PlaybillSchedule.objects.all()
    result = list(event_1) + list(event_2)
    random.shuffle(result)
    data = dict(events=result, header_name=topics['schedule'], topics=topics, active_topics=active_topics)
    return render(request, os.path.join(TheatreConfig.name, 'schedule.html'), context=data)

class TeacherListView(ListView):
    model = Teacher
    extra_context = {'header_name': topics['teachers'],
                     'topics': topics,
                     'active_topics': active_topics}


class TeacherDetailView(DetailView):
    model = Teacher


class ContactsListView(ListView):
    model = BankAccountOrganization
    template_name = os.path.join(TheatreConfig.name, 'contact.html')
    extra_context = dict(header_name=topics['contacts'], topics=topics, active_topics=active_topics)

def news():
    ...

def about():
    ...

class GalleryListView(ListView):
    model = Gallery
    extra_context = dict(header_name=topics['gallery'], topics=topics, active_topics=active_topics)

    def get_queryset(self):
        return Gallery.objects.filter(mark_deletion=False)


class GalleryCreateView(FormView):
    form_class = PhotoForm
    success_url = reverse_lazy('theatre:gallery')
    extra_context = dict(header_name=topics['gallery'], topics=topics, active_topics=active_topics)
    template_name = 'theatre/gallery_form.html'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """Сохраняем несколько файлов с изображениями"""
        images = form.cleaned_data['image']
        event = form.cleaned_data.get('event')
        for image in images:
            Gallery.objects.create(image=image, event=event)
        return super().form_valid(form)


def get_mark_deletion(request, pk):
    gallery_item = Gallery.objects.get(pk=pk)
    gallery_item.mark_deletion = True
    gallery_item.save()
    return redirect('theatre:gallery')

def deletion_form(request):
    photos = Gallery.objects.filter(mark_deletion=True).order_by('pk')
    data = dict(photos=photos, header_name=topics['gallery'], topics=topics, active_topics=active_topics)
    return render(request, os.path.join(TheatreConfig.name, 'gallery_confirm_delete.html'), context=data)

def get_deletion(request, pk):
    """Удаление объекта"""
    Gallery.objects.get(pk=pk).delete()
    return redirect('theatre:gallery-deletion-form')

def get_restore(request, pk):
    """Восстановление объекта"""
    photo = Gallery.objects.get(pk=pk)
    photo.mark_deletion = False
    photo.save()
    return redirect('theatre:gallery-deletion-form')
