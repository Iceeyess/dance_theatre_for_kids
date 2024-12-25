from django.shortcuts import render

from theatre.models import RegularClassSchedule


# Create your views here.
def index(request):
    return render(request, 'index.html')

def schedule(request):
    data = dict(regular_class_schedule=RegularClassSchedule.objects.all())
    return render(request, 'schedule.html', context=data)