from django.shortcuts import render

# Create your views here.
def users(request):
    users = render(request, 'users/users.html')