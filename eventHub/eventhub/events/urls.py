from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventsListView.as_view(), name='events'),
    path('create/', views.EventCreateView.as_view(), name='create'),
    path('<int:pk>/', views.EventDetailView.as_view(), name='event'),
    path('<int:pk>/delete/', views.EventDeleteView.as_view(), name='delete'),
]