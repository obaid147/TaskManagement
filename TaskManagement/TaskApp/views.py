from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    all_tasks = Task.objects.all()
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            my_task = form.save()
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            messages.success(request, f"{my_task} Added!")
        return redirect("/")
    context = {
        'all_tasks': all_tasks,
        'form': form,
        'title': 'Manage Tasks',
        'heading': 'Task Management'
    }
    return render(request, 'TaskApp/index.html', context)


def update(request):
    pass
