from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('about', views.about, name='about'),
    path('registrations/', include('registrations.urls')),
]