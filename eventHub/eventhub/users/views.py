from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import User
from .form import UserForm
from main.utils import FilterManager

# Create your views here.
"""
альтернативний спосіб вибрати список користувачів, без використання класу ListView
def users(request):
    users = User.objects.all()
    return render(request, 'users/users.html', {"users": users})
"""



class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/create.html'

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, f"Користувач {user.full_name} доданий успішно!")
        return render(self.request, self.template_name, {'form': self.form_class()})


class UserListView(ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = 'users'

    def get_queryset(self):
        users = super().get_queryset()
        return FilterManager.apply_filters(users, self.request, ['full_name', 'email'])


class UserDetailView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserForm(instance=user)
        return render(request, 'users/user.html', {'user': user, 'form': form})

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Дані оновлено успішно!")
            return redirect('user', pk=user.pk)
        return render(request, 'users/user.html', {'user': user, 'form': form})

class UserDeleteView(View):
    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        messages.success(request, "Користувач видалений успішно!")
        return redirect('users')


