from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import User
from .form import UserForm

# Create your views here.
def users(request):
    return render(request, 'users/users.html')




class UserCreateView(CreateView):
    model = User
    form_class = UserForm