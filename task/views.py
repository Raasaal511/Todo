from django.shortcuts import render

from .models import Task


def home(request):
    tasks = Task.objects.all()

    return render(request, 'task/home.html', {'tasks': tasks})
