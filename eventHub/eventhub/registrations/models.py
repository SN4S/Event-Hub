from django.db import models
from users.models import User
from events.models import Event

# Create your models here.
class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="registrations")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="registrations")
    status_choices = [
        ('pending', 'Очікується'),
        ('confirmed', 'Підтверджено'),
        ('canceled', 'Скасовано'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='pending')

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user.full_name} -> {self.event.name} ({self.status})"