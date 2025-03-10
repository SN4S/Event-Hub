from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListView.as_view(), name='users'),
    path('create/', views.UserCreateView.as_view(), name='create-users'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='user'),
    path('<int:pk>/delete/', views.UserDeleteView.as_view(), name='delete-user'),
]