from django import forms
from .models import Event
from django.forms import TextInput


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'name',
            'description',
            'is_finished'
        ]

        widgets = {
            'name': TextInput(attrs ={ 
            'class' : 'form-control',
            'placeholder': "Введіть назву."
            }),
            'description': TextInput(attrs ={ 
            'class' : 'form-control',
            'placeholder': "Введіть опис."
            })
        }