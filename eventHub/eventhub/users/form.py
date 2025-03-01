from django import forms
from .models import User
from django.forms import TextInput


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'full_name',
            'email'
        ]
        widgets = {
            'full_name': TextInput(attrs ={ 
            'class' : 'form-control',
            'placeholder': "Введіть повне ім'я."
            }),
            'email': TextInput(attrs ={ 
            'class' : 'form-control',
            'placeholder': "Введіть електронну пошту."
            })
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_user = getattr(self.instance, 'pk', None)

        if current_user:
            if User.objects.filter(email=email).exclude(pk=current_user).exists():
                raise forms.ValidationError('Користувач з таким email вже існує')
        else:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Користувач з таким email вже існує')

        return email