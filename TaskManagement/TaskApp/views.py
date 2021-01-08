from django.shortcuts import render
from .models import Task


def index(request):
    all_tasks = Task.objects.all()
    context = {
        'all_tasks': all_tasks,
        'title': 'Manage Tasks',
        'heading': 'Task Management'
    }
    return render(request, 'TaskApp/index.html', context)
