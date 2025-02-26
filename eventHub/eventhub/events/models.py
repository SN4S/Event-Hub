from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    is_finished = models.BooleanField()


    def str(self):
        return self.name
