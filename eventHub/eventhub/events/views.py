from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Event
from .form import EventForm
from main.utils import FilterManager

# Create your views here.
class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/create.html'

    def form_valid(self, form):
        event = form.save()
        messages.success(self.request, f"Івент {event.name} доданий успішно!")
        return render(self.request, self.template_name, {'form': self.form_class()})


class EventsListView(ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'events'

    def get_queryset(self):
        events = super().get_queryset()
        return FilterManager.apply_filters(events, self.request, ['name', 'description'])


class EventDetailView(View):
    def get(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        form = EventForm(instance=event)
        return render(request, 'events/event.html', {'event': event, 'form': form})

    def post(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Дані оновлено успішно!")
            return redirect('event', pk=event.pk)
        return render(request, 'events/event.html', {'event': event, 'form': form})

class EventDeleteView(View):
    def post(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        event.delete()
        messages.success(request, "Івент видалений успішно!")
        return redirect('events')


