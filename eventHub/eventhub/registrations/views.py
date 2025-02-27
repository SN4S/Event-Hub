from django.shortcuts import render, get_object_or_404, redirect
from events.models import Event
from users.models import User
from .models import Registration
from django.contrib import messages
from main.utils import FilterManager


# Create your views here.

def event_registration(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    registered_users = User.objects.filter(registrations__event=event).distinct()

    users = User.objects.exclude(id__in=registered_users.values_list('id', flat=True))

    users = FilterManager.apply_filters(users, request, ['full_name', 'email'])

    if request.method == "POST":
        user_ids = request.POST.getlist('user_ids')
        if user_ids:
            for user_id in user_ids:
                user = User.objects.get(id=user_id)
                Registration.objects.create(user=user, event=event)
            messages.success(request, "Учасників додано успішно!")
        return redirect('event_registration', event_id=event.id)

    return render(request, 'registrations/event_registrations.html', {
        'event': event,
        'registered_users': registered_users,
        'users': users,
    })


def remove_registration(request, event_id, user_id):
    if request.method == "POST":
        registration = get_object_or_404(Registration, event_id=event_id, user_id=user_id)
        registration.delete()
        messages.success(request, "Учасника успішно видалено з івенту!")

    return redirect('event_registration', event_id=event_id)