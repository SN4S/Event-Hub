from django.urls import path
from . import views

urlpatterns = [
    path('<int:event_id>/', views.event_registration, name='event_registration'),
    path('<int:event_id>/remove/<int:user_id>/', views.remove_registration, name='remove_registration'),

]