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
            messages.success(request, f"{my_task} Added!")
        return redirect("/")
    context = {
        'all_tasks': all_tasks,
        'form': form,
        'title': 'Manage Tasks',
        'heading': 'Task Management'
    }
    return render(request, 'TaskApp/index.html', context)


def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Updated!")
        return redirect("/")

    context = {
        'form': form,
        'title': 'Update-Task',
        'heading': 'Task Update',
    }
    return render(request, 'TaskApp/update.html', context)


def delete(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        messages.info(request, f"{task} Deleted!")
        return redirect('/')
    context = {
        'task': task,
        'title': 'Delete Task',
        'heading': 'Delete Task',
    }
    return render(request, 'TaskApp/delete.html', context)

