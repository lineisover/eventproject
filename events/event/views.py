from django.http import HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404, render

from .forms import EventForm
from .models import Event


def event_list(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'event/list.html', context)


def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    context = {
        'event': event
    }
    return render(request, 'event/detail.html', context)


def event_edit(request, id=1):
    event = get_object_or_404(Event, pk=id)
    if request.method == 'POST':
        event.title = request.POST.get('title')
        event.description = request.POST.get('description')
        event.date_time = request.POST.get('date_time')
        event.location = request.POST.get('location')
        event.save()
        context = {
            'form': EventForm(initial={'title': event.title,
                                       'description': event.description,
                                       'date_time': event.date_time,
                                       'location': event.location},),
            'event': event,
        }
        return render(request, 'event/edit.html', context)
    else:
        context = {
            'form': EventForm(initial={'title': event.title,
                                       'description': event.description,
                                       'date_time': event.date_time,
                                       'location': event.location},),
            'event': event,
        }
        return render(request, 'event/edit.html', context)


def event_delete(request, id):
    event = get_object_or_404(Event, pk=id)
    event.delete()
    return HttpResponsePermanentRedirect('/events')
