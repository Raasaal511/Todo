from django.shortcuts import render
from django.urls import reverse

from .models import Task
from .forms import TaskForm


def home(request):
    tasks = Task.objects.all().order_by('complete')
    form = add_task(request)

    return render(request, 'task/home.html', {'tasks': tasks, 'form': form})


def add_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

            return reverse('home')

    return form
