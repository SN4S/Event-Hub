from django import forms
from .models import User

class UserForm(forms.ModelForm):
    def clean_email(self):
        class Meta:
            model = User
            fields = [
                'full_name',
                'email'
            ]

        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Користувач з таким email вже існує')
        return email